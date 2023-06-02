import requests


def get_device(url, deviceId: str, headers={}):
    resp = requests.get(url + '/user/devices/' + deviceId, headers=headers)
    return resp
