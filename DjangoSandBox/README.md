# DjangoSandBox #

A collection of examples for Django from [my blog](https://lukewickstead.wordpress.com/2015/04/19/python-django) 


## Installation ##

To install the required dependant libraries run:

``` bash
pip install -r requirements.txt
```

Ensure Django has been installed correctly:

``` bash
$ python -c "import django; "import django; print(django.get_version())"
```

## Set Up ##

By default we are using SQLite 3 which is fine for development purposes.

To create the db and schema run:

``` bash
python manage.py migrate
python manage.py makemigrations formsintroduction helloworld modelsadvanced modelsintroduction viewsintroduction
python manage.py migrate
```

To create a super user

``` bash
$ python manage.py createsuperuser --username=user --email=user@foo.com
```

## Projects and Apps ##

To create a project:

``` bash
$ python django-admin startproject mysite
```

To create an app:

``` bash
python manage.py startapp myapp
```

You then need to register the app within the INSTALLED_APPS of the settings.py found within the project.

## Django/Python shell ##

Django extends the Python shell allowing for better interaction with Django/

``` bash
$ python manage.py shell
```

Or with a custom settings file:

``` bash
$ python manage.py shell --settings=DjangoSandBox.settings
```

## Starting The Development Server ###

``` bash
$ python manage.py runserver
```

Or with a custom settings file:

``` bash
$ django-admin runserver --settings=DjangoSandBox.settings
```

To kill the development server in case ctlr-c does not work:

```bash 
$ ps auxw | grep runserver
$ kill ### (Process # from previous command)
```

## Models ##

As shown above to create initial schema for all registered non local apps:

``` bash
$ python manage.py migrate
```

After making changes to models you need to make make migrations with the makemigrations and then apply them with the 
migrate command.

You can view the made migrations with the sqlmigrate command and also validate the migrations will work with the check
command.

``` bash
$ python manage.py makemigrations myapp
$ python manage.py sqlmigrate myapp 0001
$ python manage.py check myapp
$ python manage.py migrate
```


## Tests ##

Tests can be run something like this though PyCharm handles all this for me so you might need to play around.

```
$ python manage.py test --settings=DjangoSandBox.DjangoSandBox.config.test
```

## Coverage ##

Test coverage can be run something like this though PyCharm handles all this for me so you might need to play around.

``` bash
python coverage run manage.py test  --settings=DjangoSandBox.DjangoSandBox.config.test
python coverage html --include="$SITE_URL*" --omit="admin.py"
```


