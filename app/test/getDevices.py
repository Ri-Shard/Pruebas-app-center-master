import requests


def get_devices(url, headers={}):
    resp = requests.get(url + '/user/devices/', headers=headers)
    return resp
