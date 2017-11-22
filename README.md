# softdev-project-1
SoftDev Project 01 with Queenie Xiang, Jasper Cheung, Leo Liu

## U N I

## Launch Instructions

### 1. Clone this repository

#### ssh:
`git clone git@github.com:yhelen-stuy/softdev-project-1.git`

#### https:
`git clone https://github.com/yhelen-stuy/softdev-project-1.git`

### 2. Procure API keys

#### Food To Fork:
Go to the [Food2Fork](https://food2fork.com/about/api)
Sign up and request an API key
Get said key in e-mail

#### Zomato:
Go to the [Zomato API page](https://developers.zomato.com/api)
Request an API key
Get said key in e-mail

Save both keys in `.secret_key.txt` in the same directory as app.py

### 3. Prepare for launch

#### Virtualenv
We recommend you use an virtual environment to install dependencies for this site.

[To install virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
[To create an virtualevn](https://virtualenv.pypa.io/en/stable/reference/#virtualenv-command)
To activate virtualenv in a Unix-based system:
`$ . <name of virtualenv>/bin/activae`

#### Install dependencies
With an activated virtualenv:
`pip install flask`
`pip install requests`

### 4. Launch
In the repository for this site:
`python app.py`
In a browser, navigate to:
`localhost:5000`