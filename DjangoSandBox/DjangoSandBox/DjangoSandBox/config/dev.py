DEBUG = True
TEMPLATE_DEBUG = True

# Reference:
# https://docs.djangoproject.com/en/1.8/topics/logging/

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'ERROR',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'helloworld': {
            'handlers': ['console', 'file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
