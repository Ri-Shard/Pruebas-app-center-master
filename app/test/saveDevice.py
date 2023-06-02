import json
import requests


def save_device(url, userId: str, headers={}, data={}):
    resp = requests.post(url + '/users/' + userId +
                         '/devices/register', headers=headers, data=json.dumps(data))
    return resp
