import requests


def delete_device(url, deviceId: str, headers={}):
    resp = requests.delete(url + '/user/devices/' + deviceId, headers=headers)
    return resp
