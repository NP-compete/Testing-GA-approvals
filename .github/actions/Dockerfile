# Base image 
FROM python:3.10.4-alpine3.15

# installes required packages for our script


# Copies your code file  repository to the filesystem 
COPY entrypoint.py /entrypoint.py

# change permission to execute the script and
RUN chmod +x /entrypoint.py

# file to execute when the docker container starts up
ENTRYPOINT ["/entrypoint.py"]