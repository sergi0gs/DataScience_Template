from asyncio import subprocess
import os
from subprocess import PIPE
from sys import stderr, stdout

if '{{ cookiecutter.project_packages }}' == 'All':
    print("hola")
    os.system("pip install -r requirements.txt")
