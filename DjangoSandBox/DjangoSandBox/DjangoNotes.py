# TODO: Logging, Templates, Indexes, Static, AJAX, Admin, Layout, Requirements, Notes, Imports, GitHub

# db.sqlite3 Username/Password = admin/Password
# $ python manage.py createsuperuser --username=user --email=user@foo.com

# Check the version of Django
# python -c "import django; "import django; print(django.get_version())"


# Create a project
# python django-admin startproject mysite

# Create an app
# python manage.py startapp myaPP

# Create iniital schema required for all apps
# python manage.py migrate


# Make migrations, view migrations, check app for migrations, migrate
# python manage.py makemigrations myapp
# python manage.py sqlmigrate myapp 0001
# python manage.py check myapp
# python manage.py migrate

# Django/Python shell
# python manage.py shell
# python manage.py shell --settings=DjangoSandBox.settings

# Start development server
# python manage.py runserver
# django-admin runserver --settings=DjangoSandBox.settings

# Stop development run server
# ps auxw | grep runserver
# kill (Process # from previous command)

# pip freeze
# pip install -r requirements.txt

# virtualenvwrapper
# $ mkvirtualenv myenv
# $ workon myenv

# $ source myenv/bin/activate
# $ pip freeze
#
# requirements.txt
# coverage==3.7.1
# Django==1.8.2
# docutils==0.12
# Sphinx==1.3.1
# Unipath==1.1

# Coverage
# coverage run --source='.' manage.py test myapp

# Coverage
# coverage run manage.py test --settings=project.app.settings.test
# coverage html --include="$SITE_URL*" --omit="admin.py"

# Tests
# python manage.py test --settings=DjangoSandBox.DjangoSandBox.config.test


# git remove .idea
# git rm --cached -r .idea
# git commit -m "Remove config"
# git push origin master
