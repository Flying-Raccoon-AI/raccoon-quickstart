import os
import shutil
import subprocess


def setup_server(api_type, language):
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    project_dir = f"raccoon-{language}-server"
    source_dir = os.path.join(BASE_DIR, f"../examples/{language}/{language}-{api_type}-server")

    shutil.copytree(source_dir, project_dir, dirs_exist_ok=True)

    if language == "node":
        os.chdir(project_dir)
        subprocess.run(["npm", "install"])
    elif language == "python":
        os.chdir(project_dir)
        subprocess.run(["python3", "-m", "venv", "venv"])
        subprocess.run(["./venv/bin/pip", "install", "-r", "requirements.txt"])
