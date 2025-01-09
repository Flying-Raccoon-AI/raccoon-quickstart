FROM python:3.8-slim

# set a directory for the app
WORKDIR /code

# layer caching for faster builds
COPY ./requirements.txt /code/requirements.txt
# install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code


CMD streamlit run --server.port 5000 --server.address 0.0.0.0 app.py