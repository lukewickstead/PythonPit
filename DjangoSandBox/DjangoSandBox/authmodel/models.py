# Reference:
#
# https://docs.djangoproject.com/en/1.8/topics/auth/
# https://docs.djangoproject.com/en/1.8/topics/auth/default/

# By default the user class is django.contrib.auth.models.User and is found within the auth_user table.
# It has the following fields: username, password, email, first_name, last_name
#
# If the table does not suit your purposes you can:
#
# 1: Create a new table with the additional fields and join back to it:
#           user = models.OneToOneField(settings.AUTH_USER_MODEL)
#
# 2: Subclass AbstractUser or BaseUserManager if you prefer a more minimalist approach and then register the model in
#    the settings.py:
#           AUTH_USER_MODEL = "authapp.NewAuthUser"


# There are permission sets and groups which can add granularity
# @loging_required or login_reqauired directsz to  settings.LOGIN_URL, which defaults to
# http://127.0.0.1:8000/accounts/login/?next=/auth/
#
# Note
# The login_required decorator does NOT check the is_active flag on a user.
# @permission_required('polls.can_vote', login_url='/loginpage/')
