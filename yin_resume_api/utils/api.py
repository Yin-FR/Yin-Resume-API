import requests


def get_data_from_url(url, headers={}, params={}) -> tuple:
    response = requests.get(url, headers=headers, params=params)
    status = response.status_code
    if status == 200:
        data = response.json()
    else:
        data = "Failed"
    return status, data