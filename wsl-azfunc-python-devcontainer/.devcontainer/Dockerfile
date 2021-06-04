# Find the Dockerfile for mcr.microsoft.com/azure-functions/python:3.0-python3.8-core-tools at this URL
# https://github.com/Azure/azure-functions-docker/blob/master/host/3.0/buster/amd64/python/python38/python38-core-tools.Dockerfile
ARG VARIANT="3.8"
FROM mcr.microsoft.com/azure-functions/python:3.0-python${VARIANT}-core-tools
RUN sudo apt-get update
RUN sudo apt install python3-pip -y