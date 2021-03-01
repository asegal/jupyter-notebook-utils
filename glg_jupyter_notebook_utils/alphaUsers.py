# Standard library imports
import os
import pandas as pd

# Third party imports
import requests

# Local imports
from glg_jupyter_notebook_utils.session import get_session_token

ALPHA_USERS_URL = os.environ.get('CX_ALPHA_USERS_URL')
TRIAL_CONTACTS_URL = os.environ.get('CX_TRIAL_CONTACTS_URL')
TRIAL_CLIENTS_URL = os.environ.get('CX_TRIAL_CLIENTS_URL')
APP_TOKEN = os.environ.get('CX_ANALYTICS_APP_TOKEN')


def get_alpha_users():
    PARAMS = {}
    if APP_TOKEN is not None:
        PARAMS['jwt'] = get_session_token(APP_TOKEN)
    r = requests.get(ALPHA_USERS_URL, params=PARAMS, timeout=3600)
    results = r.json()
    return results


def get_trial_contacts():
    PARAMS = {}
    if APP_TOKEN is not None:
        PARAMS['jwt'] = get_session_token(APP_TOKEN)
    r = requests.get(TRIAL_CONTACTS_URL, params=PARAMS, timeout=3600)
    results = r.json()
    return results


def get_trial_clients():
    PARAMS = {}
    if APP_TOKEN is not None:
        PARAMS['jwt'] = get_session_token(APP_TOKEN)
    r = requests.get(TRIAL_CLIENTS_URL, params=PARAMS, timeout=3600)
    results = r.json()
    return results
