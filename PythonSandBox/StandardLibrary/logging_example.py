# logging_example.py
#
# Logging Example
#
# https://docs.python.org/3/howto/logging.html
#
# Level / When Used
# DEBUG:        Something strange is going on!
# INFO:         Meh
# WARNING:      Worth a try
# ERROR:        Ahh crap
# CRITICAL:     F3ck!!!!

import logging


def do_log_example():
    logging.debug('Debug Info')
    logging.info('Info')
    logging.warning('Warning')
    logging.error('Error')
    logging.critical('Critical Error')

# These should only be set once.

# Setting report level
# logging.basicConfig(level=logging.WARNING)   # Set report level
# logging.basicConfig(level=logging.DEBUG)   # Set report level

# Log to an external file; appending each app run
# logging.basicConfig(filename='log.txt',level=logging.DEBUG)

# Log to an external file: no appendage each app run
# logging.basicConfig(filename='log.txt',level=logging.DEBUG, filemode="w")

# Log prefixed with date time
# logging.basicConfig(format='%(asctime)-15s %(message)s')

# logging.basicConfig(format='%(asctime)-15s %(ip)s %(user)-8s %(message)s')
# logging.critical('Critical %s', 'Error', extra = {'ip': '192.168.0.1', 'user': 'luke'})


do_log_example()
