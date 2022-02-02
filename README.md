# Data Science Template
DataScience Template that you can download to use for your projects.

## Requirements:

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html): 

## Steps
### Install Cookiecutter chanel:
``` bash
conda config --add channels conda-forge
``` 

### Create a virtual environment
``` bash 
conda create --name [environment_name] cookiecutter=1.7.3
```

## Create a new project

In a folder where you want to download your template:

```bash
cookiecutter https://github.com/sergi0gs/DataScience_Template.git
```

## Structure
```bash
├── classes                 <- POO directory
│   └── __init__.py
├── data                    
│   ├── final               <- Final data for use in the model training
│   ├── processed           <- Data that has been transformed and cleaned.
│   └── raw                 <- Original data
├── database
│   ├── mysql               <- Directory with your Mysql queries
│   └── sql                 <- Directory with your SQL Server queries
├── functions
│   ├── get_data            <- Scripts to download or generate data
│   │   └── __init__.py
│   ├── __init__.py
│   ├── process             <- Scripts to process data
│   │   └── __init__.py
│   ├── train_fit_models    <- Scripts to train, fit, predict and measure your accuracy.
│   │   └── __init__.py
│   ├── visualization       <- Scripts to make visualizations
│   │   └── __init__.py
│   └── web_scraping        <- Scripts make web scraping
│       └── __init__.py
├── LICENCE
├── main.py                 <- Final script for your project. You can create more if you want to separate process
├── models                  <- Directory with your trained models. Ready to implement
├── notebooks               <- Jupyter notebooks, you can create more of it if needed
│   ├── 1.0_data.ipynb
│   ├── 2.0_clean.ipynb
│   ├── 3.0_transform.ipynb
│   ├── 4.0_train_fit_models.ipynb
│   └── 5.0_accuracy.ipynb
├── README.md               
└── requirements.txt        <- File with the basics packages that you maybe need
```

## Install requirements packages
Normally, you have to install with:
```bash
pip install -r requirements.txt
```
but in this case, the template install it for you.

## Credits

This project was influenced by [Cookiecutter Conda Data Science](https://github.com/jvelezmagic/cookiecutter-conda-data-sciencee), and the course [Curso de Configuración Profesional de Entorno de Trabajo para Ciencia de Datos](https://platzi.com/cursos/entorno-ciencia-datos/) of Platzi.
