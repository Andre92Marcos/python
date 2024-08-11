# Python Virtual Environments

## Overview

Virtual environments allows us to use different python versions and packages at the same time, for differrent projects.

So if one project with need python 2 and in another we need python 3 we don't have to unninstall and install different versions of python everytime we change project, we can just use a virtual environment. Same thing goes for different packages versions like numpy or pandas.

https://medium.com/@vasanthabalaji/venv-or-virtualenv-671113544237

https://realpython.com/python-virtual-environments-a-primer/


## Creating a virtual env with virtualenv

	virtualenv <protject_name>

You can also specify the python version you want to use:

	virtualenv -p python3.8 <env_name>

To activate the virtual env:

	source <project_name>/bin/activate

To check if we are in the virtual env successfully do:

	pip list

We should see only three packages installed

## Deactivating the env

Simply do:

	deactivate

And now the env is deactivated. You can do pip list again to confirm.