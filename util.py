import requests


def requests_get(base_url, params=None, headers=None):
    response = requests.get(base_url, params=params, headers=headers)
    if response.status_code == 200:
        return response
    else:
        print(f'** Request failed: status={response.status_code}, url={base_url}')
        return None



