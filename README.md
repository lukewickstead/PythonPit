# PythonPit #

Examples for Python and Django from [my blog](https://lukewickstead.wordpress.com/2015/04/19/python-django).

There are two example sets; PythonSandBox and DjangoSandBox, please read the README.md for each project for additional 
setup and configuration information.

PythonSandBox has examples of Python and the standard library, DjangoSandBox has examples of Django.


## Python 3.4 ##

I was using Python 3.4 as this was the latest version available on my Linux box by default. You might want to check
which version is in your path:

``` bash
$ which python
```

## Installation ##

To install the required dependant libraries use the requirements.txt contained in both PythonSandBox and DjangoSandBox:

```
pip install -r requirements.txt
```

To generate a requirements file or to see what libraries you current python environment has you can run pip freeze:

```
pip freeze
pip freeze > requirements.txt
```

More information about [PIP](http://pip-installer.org).

   
## Virtualenv, VirtualEnvWrapper, PyCharm ##

I personally use [PyCharm](https://www.jetbrains.com/pycharm/) which handles virtual environments automatically. 
There is a community version for free though the paid version is worth the money especially if you are going to work on
Django.

Otherwise I would recommend [Virtualenv](http://virtualenv.org) which allows multiple isolate Python environments.

I would also recommend [VirtualEnvWrapper](https://virtualenvwrapper.readthedocs.org/en/latest/) which allows easier 
switching between virtual python environments.

With virtualenv:

```
pip install virtualenv
cd project_dir
virtualenv myvenv
$ source ~/.virtualenvs/myenv/bin/activate  
```

With virtualenvwrapper

```
$ pip install virtualenvwrapper
mkvirtualenv myenv
$ workon myenv                              
```

More information can be found [here](http://docs.python-guide.org/en/latest/dev/virtualenvs)