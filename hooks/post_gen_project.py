from asyncio import subprocess
import os
from subprocess import PIPE
from sys import stderr, stdout

print("Este es el despues de instalar el template")
#dir_here = os.getcwd()
#dir_requirementes = os.path.join(dir_here, os.pardir, "{{ cookiecutter.project_slug }}","requirements.txt")

if '{{ cookiecutter.project_packages }}' == 'All':
    print("hola")
    os.system("pip install -r requirements.txt")
