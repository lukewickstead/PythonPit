# urllib_request_example.py
#
# Urllib Request_example
#
# This module provides a high-level interface for fetching data across the World Wide Web

from urllib.request import urlopen, HTTPError

try:

    for x in urlopen("http://www.google.com"):
        print(x)
except HTTPError as error:
    contents = error.read()