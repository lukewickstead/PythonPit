
# Initial Migration
# python3.3 manage.py migrate


# Make model changes then:
#   Make Migrations for polls app:
#       python3.3 manage.py makemigrations polls
#   View Migration Script:
#       python3.3 manage.py sqlmigrate polls 0001
#   Migrate:
#       python3.3 manage.py migrate

# Django has its down timezone object; useful for a website which is accessible all over the world?!?!
# timezone.now()

# admin/Password