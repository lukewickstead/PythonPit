# Django’s default behavior is autocommit mode; each touch of the database is immediately committed.
# We can change to a transaction to ensure all database touches either pass or fail together
# Transactions can be nested; failure only rolls back database touches which are within scope
#
# Reference:
# https://docs.djangoproject.com/en/1.8/topics/db/transactions

from django.db import transaction, IntegrityError


@transaction.atomic
def a_function():
    pass


# and as a context manager:
#
# from django.db import transaction
#
def another_function():
    try:
        with transaction.atomic():
            # All code is contained within a transaction
            # Automatically committing or rolling back if an exception is raised
            pass
    except IntegrityError:
        pass
        # It is important to let the with statement catch any initial exceptions raised
