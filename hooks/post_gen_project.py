from asyncio import subprocess
import os
from subprocess import PIPE
from sys import stderr, stdout

print("Este es el despues de instalar el template")
project_packages = "{{ cookiecutter.project_packages }}"

print(project_packages)
dir_here = os.getcwd()
dir_requirementes = os.path.join(dir_here, os.pardir, "{{ cookiecutter.project_slug }}","requirements.txt")

if project_packages == 1:
    subprocess.call(['pip', 'install', '-r', 'requirements.txt'])

else:
    pass
