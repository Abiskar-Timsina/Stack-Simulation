# Stack-Simulation:

#### Initial Pull
You can directly pull this directory,

```console
$ git init 
$ git remote add origin https://github.com/Abiskar-Timsina/Stack-Simulation.git
$ git pull origin master
```

#### Virtual Environment
Since, we don't have to share our virtual environment, i've excluded the "/environment" directory. For convinience, name the virtual environment; "environment"

_For Windows_ 
```console
$ python -m venv environment
```
_For Linux_ 
```console
$ python3 -m venv environment
```

To activate, 

_For Windows_
```console
$  .\environment\Scripts\activate
```
_For Linux_
```console
$  .\environment\bin\activate
```

To deactivate,

_Windows & Linux_
```console
$ deactivate
```

#### Installing the required packages
Required modules are listed in the requirements.txt file. To install,
```console
$ pip install -r ./requirements.txt
```

#### TODO:
- Better error handling
	- Error: Pop operation is used if the stack is empty.
	- Error: Stack Overflow
- Input for the size of stack.
- Exit Button.