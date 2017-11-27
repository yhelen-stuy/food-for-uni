# Food for U N I by Queenie Xiang, Jasper Cheung, Leo Liu, Helen Ye
This project allows you to search for recipes if you want to cook yourself or restaurants if you want to eat out. If you're super indecisive, we have recommendations prepared for you!

## Launch Instructions

### 1. Clone this repository

#### ssh:

```git clone git@github.com:yhelen-stuy/softdev-project-1.git ~/softdev-project-1```

#### https:

```git clone https://github.com/yhelen-stuy/softdev-project-1.git ~/softdev-project-1```

### 2. Procure API keys

#### Food To Fork:

1. Go to the [Food2Fork](https://food2fork.com/about/api)
2. Sign up and request an API key
3. Get said key in e-mail

#### Zomato:

1. Go to the [Zomato API page](https://developers.zomato.com/api)
2. Request an API key
3. Get said key in e-mail

Save both keys in `.secret_key.txt` in the same directory as app.py.
It is recommended to copy the template below and replace the YOUR_KEY_HERE fields.

```
{
  'zomato_key': 'YOUR_ZOMATO_KEY_HERE',
  'food2fork_key': 'YOUR_FOOD2FORK_KEY_HERE'
}
```

### 3. Prepare for launch

#### Virtualenv

We recommend you use an virtual environment to install dependencies for this site.

* [To install virtualenv](https://virtualenv.pypa.io/en/stable/installation/)
* [To create an virtualevn](https://virtualenv.pypa.io/en/stable/reference/#virtualenv-command)

To activate virtualenv in a Unix-based system:

```
$ . <name of virtualenv>/bin/activate
```

#### Install dependencies

With an activated virtualenv:

```
$ pip install flask
$ pip install requests
```

### 4. Launch

```
$ python ~/softdev-project-1/app.py
```

In a browser, navigate to `localhost:5000`. **ENJOY!!**
