from asyncio import subprocess
import os
from subprocess import PIPE
from sys import stderr, stdout

project_packages = "{{ cookiecutter.project_packages }}"
dir_here = os.getcwd()
dir_requirementes = os.path.join(dir_here, os.pardir, "{{ cookiecutter.project_slug }}","requirements.txt")

if project_packages == 1:
    install = subprocess.run(f"pip install -r {dir_requirementes}",
                             stdout = PIPE,
                             stderr = PIPE)

else:
    pass
