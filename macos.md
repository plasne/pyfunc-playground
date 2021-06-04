# macOS

This document describes notes from getting Azure Functions development working on a mac.

## Python version

Even after picking the 3.8 interpreter, the version still shows as 3.9 when debugging...

```log
Found Python version 3.9.5 (python3).
```

...even though the settings.json shows the correct 3.8 executible...

```json
{
    "python.pythonPath": "/usr/bin/python3",
}
```

What worked was installing...

```bash
pip install virtualenv
```

And then running...

```bash
python3 -m pip install virtualenv
python3 -m virtualenv --python=/usr/bin/python3 .venv
```

...where /usr/bin/python3 was my 3.8.2 binary. The pyvenv.cfg was changed to this...

```text
home = /Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8
implementation = CPython
version_info = 3.8.2.final.0
virtualenv = 20.4.7
include-system-site-packages = false
base-prefix = /Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8
base-exec-prefix = /Applications/Xcode.app/Contents/Developer/Library/Frameworks/Python3.framework/Versions/3.8
base-executable = /Applications/Xcode.app/Contents/Developer/usr/bin/python3
```

## Shared Memory Error

The following errors are shown in the logs whenever `func start` is run...

```log
[2021-06-02T12:36:54.660Z] Cannot create directory for shared memory usage: /dev/shm/AzureFunctions
[2021-06-02T12:36:54.660Z] System.IO.FileSystem: Access to the path '/dev/shm/AzureFunctions' is denied. Operation not permitted.
```

This is documented as an open bug here: https://github.com/Azure/azure-functions-core-tools/issues/2600.

## azure.functions [LOCAL]

The following error message was shown: `Import "azure.functions" could not be resolved`.

Installing via pip doesn't work...

```bash
pip install azure.functions
```

...results in...

```text
Requirement already satisfied: azure.functions in ./.venv/lib/python3.8/site-packages (1.7.0)
```

Changing the interpreter in VSCODE to the .venv version fixes the issue, but unfortunately this was version 3.9.5 for me.

## azure.functions [REMOTE]

The same error appears when using a devcontainer. To fix it, I had to find the path of the python 3.8 executable in the container and set the interpreter to that. I had to do this manually since the interface didn't show the correct option.

The path is `\usr\local\bin\python3`.

## Debug [REMOTE]

To debug in a dev container, you must set the linux command to run `/usr/local/bin/python3`...

```json
{
	"version": "2.0.0",
	"tasks": [
		{
			"label": "pipInstall",
			"linux": {
				"command": "/usr/local/bin/python3 -m pip install -r requirements.txt"
			},
		}
	]
}
```

If you are running in WSL, you can use an environment variable for the command, ex. `${env:LINUX_PYTHON_PATH}`. You can set an environment variable in the devcontainer.json file as `remoteEnv` (which requires a restart).
