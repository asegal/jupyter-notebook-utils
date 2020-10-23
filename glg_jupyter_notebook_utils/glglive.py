# Standard library imports
import os
import pandas as pd

# Third party imports
import requests

# Local imports
from glg_jupyter_notebook_utils.session import get_session_token

EPISTREAM_SERVICE = os.environ.get('CX_ANALYTICS_EPISTREAM_SERVICE')
APP_TOKEN = os.environ.get('CX_ANALYTICS_APP_TOKEN')


def get_glglive_query(query, params={}):
    URL = f'{EPISTREAM_SERVICE}/epiquery1/{query}'
    PARAMS = params
    HEADERS = {}
    if APP_TOKEN is not None:
        TOKEN = get_session_token(APP_TOKEN)
        HEADERS['Authorization'] = f'Bearer {TOKEN}'
    r = requests.get(URL, params=PARAMS, timeout=3600, headers=HEADERS)
    results = r.json()
    return results


def post_glglive_query(query, data={}):
    URL = f'{EPISTREAM_SERVICE}/epiquery1/{query}'
    DATA = data
    HEADERS = {}
    if APP_TOKEN is not None:
        TOKEN = get_session_token(APP_TOKEN)
        HEADERS['Authorization'] = f'Bearer {TOKEN}'
    r = requests.post(URL, data=DATA, timeout=3600, headers=HEADERS)
    results = r.json()
    return results
