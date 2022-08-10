FROM python:3.10.6-slim

# Install lizbar0 for qrcode extraction
RUN apt-get update && apt-get install -y libzbar0 

# copy all file from local to app
COPY . /app
WORKDIR /app

# create virtualenv
RUN python3 -m venv /opt/venv

# upgrade pip, install all requirements
RUN /opt/venv/bin/pip install pip --upgrade
RUN /opt/venv/bin/pip install -r requirements.txt

RUN chmod +x entrypoint.sh

# excecute commands in entrypoint bash script
CMD ["/app/entrypoint.sh"]