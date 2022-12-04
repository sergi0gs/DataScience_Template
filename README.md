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
├── README.md         <- README for the project
├── app               <- Directory of necessary content for the creatiion of the app.
│   ├── static
│   └── templates
├── app.py            <- Main file for the app.
├── classes           <- Directory of classes to develop an AI model.
│   └── __init__.py
├── data              <- Directory of data
│   ├── final
│   ├── processed
│   └── raw
├── database          <- Directory with necessary quieries for the project.
├── main.py           <- Main file for the develop an AI model.
├── models            <- Trained and serialized models, model predictions, or model summaries.
├── notebooks         <- Jupyter notebooks.
│   ├── 1.0_data.ipynb
│   ├── 2.0_clean.ipynb
│   ├── 3.0_transform.ipynb
│   ├── 4.0_train_fit_models.ipynb
│   └── 5.0_evaluation.ipynb
├── requirements.txt  <- Requirements file for necessary libraries.
├── src
│   ├── __init__.py
│   ├── build_features.py   <- Script to turn raw data into features for modeling.
│   ├── make_dataset.py     <- Script to download or generate data.
│   ├── predict_model.py    <- Script to make predictions.
│   ├── train_model.py      <- Script to train models.
│   └── utils.py            <- Script to help with common tasks.
└── test.py      <- Script to test classes and functions.
```

## Install requirements packages
Normally, you have to install with:
```bash
pip install -r requirements.txt
```
but in this case, the **template install it for you** if you press "Enter" o "1" when the system asks you *Select project_packages:*

## Credits

This project was influenced by [Cookiecutter Conda Data Science](https://github.com/jvelezmagic/cookiecutter-conda-data-sciencee), and the course [Curso de Configuración Profesional de Entorno de Trabajo para Ciencia de Datos](https://github.com/jvelezmagic/cookiecutter-conda-data-science) of Platzi.
