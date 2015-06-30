# TODO: Views (index, style), Forms/FormView, Login/Security, Web Service, Requirements file, notes, Documentation, coding style, relative imports, ajax, csv, pdf, test

# db.sqlite3 Username/Password = admin/Password

# Check the version of Django
# python -c "import django; "import django; print(django.get_version())"


# Create a project
# python django-admin startproject mysite

# Create an app
# python manage.py startapp myaPP

# Create iniital schema required for all apps
# python manage.py migrate

# Make migrations, view migrations, check app for migrations, migrate
#python manage.py makemigrations myapp
#python manage.py sqlmigrate myapp 0001
#python manage.py check myapp
#python manage.py migrate

# Django/Python shell
# python manage.py shell
# python manage.py shell --settings=DjangoSandBox.settings.local

# Start development server
# python manage.py runserver
# django-admin runserver --settings=mysite.settings

# Stop development run server
# ps auxw | grep runserver
# kill (Process # from previous command)


# Coverage
# coverage run manage.py test --settings=twoscoops.settings.test
# coverage html --include="$SITE_URL*" --omit="admin.py"

# Tests
# python manage.py test --settings=DjangoSandBox.DjangoSandBox.config.test
