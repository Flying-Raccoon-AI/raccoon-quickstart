import os
import subprocess

NODE_TEMPLATE = """
require('dotenv').config();
const express = require('express');
const axios = require('axios');
const app = express();
const port = 3000;

app.use(express.json());

app.post('{route}', async (req, res) => {{
    try {{
        const raccoonPasscode = req.headers['raccoon-passcode'];
        const secretKey = process.env.RACCOON_SECRET_KEY;

        if (!raccoonPasscode) {{
            return res.status(400).send("Missing 'raccoon-passcode' header.");
        }}

        const response = await axios.post(`{api_url}`, req.body, {{
            headers: {{
                'Content-Type': 'application/json',
                'raccoon-passcode': raccoonPasscode,
                'secret-key': secretKey
            }}
        }});
        res.json(response.data);
    }} catch (error) {{
        res.status(500).send(error.toString());
    }}
}});

app.listen(port, () => {{
    console.log(`Node.js server running on http://localhost:${{port}}`);
}});
"""

PYTHON_TEMPLATE = """
import os
from flask import Flask, jsonify, request
import requests
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

@app.route('{route}', methods=['POST'])
def call_raccoon_api():
    try:
        raccoon_passcode = request.headers.get('raccoon-passcode')
        secret_key = os.getenv('RACCOON_SECRET_KEY')

        if not raccoon_passcode:
            return "Missing 'raccoon-passcode' header.", 400

        response = requests.post(
            '{api_url}', 
            json=request.get_json(), 
            headers={{
                'Content-Type': 'application/json',
                'raccoon-passcode': raccoon_passcode,
                'secret-key': secret_key
            }}
        )
        return jsonify(response.json())
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(port=3000, debug=True)
"""

GO_TEMPLATE = """
package main

import (
    "bytes"
    "fmt"
    "io/ioutil"
    "net/http"
    "os"
    "github.com/gorilla/mux"
    "github.com/joho/godotenv"
)

func callRaccoonAPI(w http.ResponseWriter, r *http.Request) {{
    err := godotenv.Load()
    if err != nil {{
        http.Error(w, "Error loading .env file", http.StatusInternalServerError)
        return
    }}

    secretKey := os.Getenv("RACCOON_SECRET_KEY")
    raccoonPasscode := r.Header.Get("raccoon-passcode")

    if raccoonPasscode == "" {{
        http.Error(w, "Missing 'raccoon-passcode' header", http.StatusBadRequest)
        return
    }}

    body, _ := ioutil.ReadAll(r.Body)
    client := &http.Client{{}}
    req, _ := http.NewRequest("POST", "{api_url}", bytes.NewBuffer(body))
    req.Header.Set("Content-Type", "application/json")
    req.Header.Set("raccoon-passcode", raccoonPasscode)
    req.Header.Set("secret-key", secretKey)

    resp, err := client.Do(req)
    if err != nil {{
        http.Error(w, err.Error(), http.StatusInternalServerError)
        return
    }}
    defer resp.Body.Close()

    respBody, _ := ioutil.ReadAll(resp.Body)
    w.Write(respBody)
}}

func main() {{
    r := mux.NewRouter()
    r.HandleFunc("{route}", callRaccoonAPI).Methods("POST")
    fmt.Println("Go server running on http://localhost:3000")
    http.ListenAndServe(":3000", r)
}}
"""

def get_request_config(api_type):
    if api_type == "strict":
        return "/lam/:app_name/run", "https://api.flyingraccoon.tech/lam/{app_name}/run"
    elif api_type == "run":
        return "/lam/run", "https://api.flyingraccoon.tech/lam/run"
    elif api_type == "extract":
        return "/lam/extract", "https://api.flyingraccoon.tech/lam/extract"
    else:
        raise ValueError("Invalid API type.")

def write_server_files(language, route, api_url):
    if language == "node":
        content = NODE_TEMPLATE.format(route=route, api_url=api_url)
        file_name = "server.js"
    elif language == "python":
        content = PYTHON_TEMPLATE.format(route=route, api_url=api_url)
        file_name = "server.py"
    elif language == "go":
        content = GO_TEMPLATE.format(route=route, api_url=api_url)
        file_name = "server.go"
    else:
        raise ValueError("Invalid language.")

    with open(file_name, "w") as f:
        f.write(content)

    with open(".env", "w") as f:
        f.write("RACCOON_SECRET_KEY=<your_secret_key>\n")

def setup_server(api_type, language):
    route, api_url = get_request_config(api_type)

    project_dir = f"raccoon_{language}_server"
    os.makedirs(project_dir, exist_ok=True)
    os.chdir(project_dir)

    if language == "node":
        subprocess.run(["npm", "init", "-y"])
        subprocess.run(["npm", "install", "express", "axios", "dotenv"])
    elif language == "python":
        subprocess.run(["python3", "-m", "venv", "venv"])
        with open("requirements.txt", "w") as f:
            f.write("\n".join([
                "flask",
                "requests",
                "python-dotenv"
            ]))
        subprocess.run(["./venv/bin/pip", "install", "-r", "requirements.txt"])
    elif language == "go":
        subprocess.run(["go", "mod", "init", project_dir])
        subprocess.run(["go", "get", "github.com/gorilla/mux"])
        subprocess.run(["go", "get", "github.com/joho/godotenv"])

    write_server_files(language, route, api_url)
