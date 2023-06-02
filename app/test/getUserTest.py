import requests


def get_user_data(url, headers={}):
    resp = requests.get(url + '/user', headers=headers)
    return resp
