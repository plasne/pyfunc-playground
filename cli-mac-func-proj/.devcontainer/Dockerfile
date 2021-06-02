FROM mcr.microsoft.com/vscode/devcontainers/python:3.8
RUN wget -qO- https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.asc.gpg
RUN sudo mv microsoft.asc.gpg /etc/apt/trusted.gpg.d/
RUN wget -q https://packages.microsoft.com/config/debian/10/prod.list
RUN sudo mv prod.list /etc/apt/sources.list.d/microsoft-prod.list
RUN sudo chown root:root /etc/apt/trusted.gpg.d/microsoft.asc.gpg
RUN sudo sudo chown root:root /etc/apt/sources.list.d/microsoft-prod.list
RUN sudo apt-get update
RUN sudo apt-get install azure-functions-core-tools-3