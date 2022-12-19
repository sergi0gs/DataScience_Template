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
Windows: 
``` bash 
pip install cookiecutter
```

Linux:
``` bash 
pip3 install cookiecutter
```
## Install project
1) In the terminal, move to the folder where you want to download your template and write:

```bash
cookiecutter https://github.com/sergi0gs/DataScience_Template.git
```
2) If the template has been previously downloaded you will see the following message: **"You've downloaded [*template_root*] before. Is it okay to delete and re-download it? [yes]"** . To which you must answer "Yes" by pressing "Enter".
3) Write the "Project name" and "Enter".
4) Write the "Project Slug" and "Enter".
5) (optional) Write de "Project Description" and "Enter".
6) Write 1 (No - default) or 2 (Yes) if you want to download the Packages on "requirements.txt" file. Then press "Enter".
7) Select de "Project version", it is recommended to leave it at 0.0.0 by pressing "Enter".

## Structure

```bash
├── README.md         <- README for the project
├── app               <- Directory of necessary content for the creatiion of the app.
│   ├── static
│   └── templates
├── app.py            <- Main file for the app.
├── data              <- Directory of data
│   ├── final
│   ├── processed
│   └── raw
├── database          <- Directory with necessary quieries for the project.
├── main.py           <- Main file for the develop an AI model.
├── models            <- Trained and serialized models, model predictions, or model summaries.
├── notebooks         <- Jupyter notebooks.
│   ├── 1.0_get_data.ipynb
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

This project was influenced by [Cookiecutter Conda Data Science](https://github.com/jvelezmagic/cookiecutter-conda-data-science), and the course [Curso de Configuración Profesional de Entorno de Trabajo para Ciencia de Datos](https://github.com/jvelezmagic/cookiecutter-conda-data-science) of Platzi.
