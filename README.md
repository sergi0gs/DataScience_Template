# Data Science Template
DataScience Template that you can download to use for your projects.

## Requirements:

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html): 

## Steps
### Create a virtual environment (Recomendation python=3.9.13)
``` bash 
conda create --name [environment_name] python=3.9.13
```
### Activate your virtual environment
``` bash 
conda activate [environment_name] 
```
## Install cookiecutter
``` bash 
pip install cookiecutter
```
## Install project
In a folder where you want to download your template:

```bash
cookiecutter https://github.com/sergi0gs/DataScience_Template.git
```

## Structure
```bash
├── classes                           <- POO directory
│   └── __init__.py
├── data
│   ├── final                         <- Final data for use in the model training
│   ├── processed                     <- Data that has been transformed and cleaned
│   └── raw                           <- Raw data
├── database                          <- Queries directory (MySQL, SQL Server, etc)
├── functions                         <- Reusable functions for main file
│   └── __init__.py
├── main.py                           <- Final script for your project. You can create more if you want to separate process
├── models                            <- Directory with your trained models. Ready to implement
├── notebooks       
│   ├── 0.0_functions.py
│   ├── 0.0_viz_functions.py
│   ├── 1.0_data.ipynb
│   ├── 2.0_clean.ipynb
│   ├── 3.0_transform.ipynb
│   ├── 4.0_train_fit_models.ipynb
│   └── 5.0_accuracy.ipynb
├── README.md
└── requirements.txt                  <- File with the basics packages that you maybe need
```

## Install requirements packages
Normally, you have to install with:
```bash
pip install -r requirements.txt
```
but in this case, the **template install it for you** if you press "Enter" o "1" when the system asks you *Select project_packages:*

## Credits

This project was influenced by [Cookiecutter Conda Data Science](https://github.com/jvelezmagic/cookiecutter-conda-data-sciencee), and the course [Curso de Configuración Profesional de Entorno de Trabajo para Ciencia de Datos](https://github.com/jvelezmagic/cookiecutter-conda-data-science) of Platzi.
