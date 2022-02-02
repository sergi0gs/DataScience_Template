# Data Science Template
DataScience Template that you can download to use for your projects.

## Requirements:

- [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/download.html)
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html): 

After create your virtual environment, install Cookiecutter with:

``` bash
pip install cookiecutter
```

or

``` bash
conda install -c conda-forge cookiecutter
```

## Create a new project

In a folder where you want to download your template:

```bash
cookiecutter https://github.com/sergi0gs/DataScience_Template.git
```

## Structure
```bash
├── classes                 <- Classes directory
│   └── __init__.py
├── data
│   ├── final
│   ├── processed
│   └── raw
├── database
│   ├── mysql
│   └── sql
├── execution
├── functions
│   ├── get_data
│   │   └── __init__.py
│   ├── __init__.py
│   ├── process
│   │   └── __init__.py
│   ├── train_fit_models
│   │   └── __init__.py
│   ├── visualization
│   │   └── __init__.py
│   └── web_scraping
│       └── __init__.py
├── LICENCE
├── main.py
├── models
├── notebooks
│   ├── 1.0_data.ipynb
│   ├── 2.0_clean.ipynb
│   ├── 3.0_transform.ipynb
│   ├── 4.0_train_fit_models.ipynb
│   └── 5.0_accuracy.ipynb
├── README.md
└── requirements.txt
```