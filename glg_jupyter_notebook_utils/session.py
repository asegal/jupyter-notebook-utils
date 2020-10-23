# Third party imports
import requests


def get_session_token(APP_TOKEN):
    if APP_TOKEN is None:
        raise Exception('Missing APP_TOKEN')
    jwt_url = f'https://services.glgresearch.com/auth/getSessionToken/{APP_TOKEN}'
    r = requests.get(jwt_url)
    result = r.json()
    if result['token'] is None:
        raise Exception('No token returned')
    return result['token']
