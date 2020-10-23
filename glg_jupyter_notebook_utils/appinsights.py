# Standard library imports
import json
import os

# Third party imports
import pandas as pd
import requests

EPISTREAM_SERVICE = os.environ.get('CX_ANALYTICS_EPISTREAM_SERVICE')
APPLICATION_INSIGHTS_APP_ID = os.environ.get(
    'CX_ANALYTICS_APPLICATION_INSIGHTS_APP_ID')
APPLICATION_INSIGHTS_KEY = os.environ.get(
    'CX_ANALYTICS_APPLICATION_INSIGHTS_KEY')


def get_app_insights_query(query):
    URL = f'https://api.applicationinsights.io/v1/apps/{APPLICATION_INSIGHTS_APP_ID}/query'
    PARAMS = {'query': query}
    HEADERS = {'x-api-key': APPLICATION_INSIGHTS_KEY}
    r = requests.get(URL, headers=HEADERS, params=PARAMS)
    results = r.json()
    primary_result = results['tables'][0]

    columns = [x['name'] for x in primary_result['columns']]
    rows = primary_result['rows']
    hasCustomDimensions = False

    df = pd.DataFrame(rows, columns=columns)
    for i, row in df.iterrows():
        if hasattr(row, 'customDimensions'):
            hasCustomDimensions = True
            customDimensions = json.loads(row.customDimensions)
            for key, value in customDimensions.items():
                if key not in df.columns:
                    df[key] = ""
                df.at[i, key] = value
        continue
    if hasCustomDimensions:
        df.drop(columns=['customDimensions'], inplace=True)
    return df
