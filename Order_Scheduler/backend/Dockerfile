FROM python:3.8-slim

# set a directory for the app
WORKDIR /code

RUN apt update -y
RUN apt install build-essential -y
RUN apt-get install manpages-dev -y
RUN apt-get install -y supervisor
RUN chmod -R 777 /code
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*


COPY ./requirements.txt /code/requirements.txt

# install dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code


# tell the port number the container should expose
# needs to be set else Celery gives an error (because docker runs commands inside container as root)
ENV C_FORCE_ROOT=1

# run supervisord
CMD ["/usr/bin/supervisord"]

