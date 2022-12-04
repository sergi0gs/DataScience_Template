from asyncio import subprocess
import os
from subprocess import PIPE
from sys import stderr, stdout

if '{{ cookiecutter.project_packages }}' == 'Yes':
    print("Install Basic Packages")
    os.system("pip install -r requirements.txt")

else:
    print("No Install Packages")