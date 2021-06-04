# AFTER CLONING INTO WSL

1. From WSL, use vscode to open this sub-directory.

1. Install Remote - Container Extension

1. Hit F1

    - Select `> Remote-Containers: Open Folder in Container`
    - Choose this sub-directory
    - Wait for devcontainer to build (restart if vscode crashes for any reason; select 'allow' if firewall permissions are prompted)

1. Run `/usr/local/py-utils/venvs/virtualenv/bin/python  -m pip install --upgrade pip` to install latest pip to virtual environment

1. Open `./pyfunc-HttpTrigger1/_init_.py`

1. Hit F5 to run the Azure Function

 - Azure function start-up progress should be visible in `Output` tab of the terminal. If successful, an http link to the azure function should be available in the `Output` tab of the terminal


# FROM SCRATCH