from requests import Response
from app.test.deleteDevice import delete_device
from app.test.getDevice import get_device
from app.test.getDevices import get_devices
from app.test.getUserTest import get_user_data
from app.test.saveDevice import save_device

apiKey = '9c36d9ea480dff4fb731dc1cb1e963fa9ba434f0'
baseURL = 'https://api.appcenter.ms/v0.1'


def formatResponse(resp: Response, testName: str):
    if resp.status_code < 400:
        print(chr(27) + "\n[1;32m"+"Test -" + testName + "- pass", )
    else:
        print(chr(27) + "\n[1;31m"+"Test -" + testName + "- failed", )
        data = resp.json()
        print(data)
        print('\n')


def executeTest():
    print(chr(27) + '[1;33m' + 'Get User')
    userValidToken()
    userInvalidToken()
    userNotToken()
    print(chr(27) + '[1;33m' + 'Save device')
    saveDevice()
    saveDeviceNoBody()
    saveDeviceNoUserId()
    print(chr(27) + '[1;33m' + 'Get device')
    getDevice()
    getDeviceNotFound()
    getDeviceWrongToken()
    print(chr(27) + '[1;33m' + 'Get devices')
    getDevices()
    getDevicesNotToken()
    getDevicesInvalidToken()
    print(chr(27) + '[1;33m' + 'Get devices')
    deleteDevice()
    deleteDeviceWrongId()
    deleteDeviceNoToken()


def userValidToken():
    resp = get_user_data(
        baseURL, {'accept': 'application/json', "X-API-Token": apiKey})
    formatResponse(resp, 'valid token')


def userInvalidToken():
    resp = get_user_data(
        baseURL, {'accept': 'application/json', "X-API-Token": apiKey + '123'})
    formatResponse(resp, 'invalid token')


def userNotToken():
    resp = get_user_data(
        baseURL, {'accept': 'application/json'})
    formatResponse(resp, 'without token')


def saveDevice():
    payload = {'udid': '1',
               'model': 'S20',
               'os_build': '1',
               'os_version': '12.2.5',
               'serial': '',
               'imei': '',
               'owner_id': 'string'}
    resp = save_device(
        baseURL, 'f997d625-0bef-45b4-a5b3-e7cd43973fd6', {'accept': 'application/json', "X-API-Token": apiKey, "Content-Type": "application/json"}, payload)
    formatResponse(resp, 'save device')


def saveDeviceNoBody():
    resp = save_device(
        baseURL, 'f997d625-0bef-45b4-a5b3-e7cd43973fd6', {'accept': 'application/json', "X-API-Token": apiKey, "Content-Type": "application/json"})
    formatResponse(resp, 'save device without payload')


def saveDeviceNoUserId():
    payload = {'udid': '1',
               'model': 'S20',
               'os_build': '1',
               'os_version': '12.2.5',
               'serial': '',
               'imei': '',
               'owner_id': 'string'}
    resp = save_device(
        baseURL, 'f997d625-0bef-45b4-e7cd43973fd6', {'accept': 'application/json', "X-API-Token": apiKey, "Content-Type": "application/json"}, payload)
    formatResponse(resp, 'save device with wrong user id')


def getDevice():
    resp = get_device(baseURL, '1', {
        'accept': 'application/json', "X-API-Token": apiKey, "Content-Type": "application/json"})
    formatResponse(resp, 'get device')


def getDeviceWrongToken():
    resp = get_device(baseURL, '1', {
        'accept': 'application/json', "Content-Type": "application/json", "X-API-Token": apiKey + '123'})
    formatResponse(resp, 'get device with wrong token')


def getDeviceNotFound():
    resp = get_device(baseURL, '3', {
        'accept': 'application/json', "X-API-Token": apiKey, "Content-Type": "application/json"})
    formatResponse(resp, 'device not found')


def getDevices():
    resp = get_devices(baseURL, {'accept': 'application/json',
                       "X-API-Token": apiKey, "Content-Type": "application/json"})

    formatResponse(resp, 'get devices')


def getDevicesNotToken():
    resp = get_devices(
        baseURL, {'accept': 'application/json', "Content-Type": "application/json"})
    formatResponse(resp, 'get devices without token')


def getDevicesInvalidToken():
    resp = get_devices(baseURL, {'accept': 'application/json',
                       "X-API-Token": apiKey + '1assa23', "Content-Type": "application/json"})
    formatResponse(resp, 'get devices with invalid token')


def deleteDevice():
    resp = delete_device(baseURL, '1', {'accept': 'application/json',
                                        "X-API-Token": apiKey, "Content-Type": "application/json"})
    formatResponse(resp, 'delete device')


def deleteDeviceWrongId():
    resp = delete_device(baseURL, '3', {'accept': 'application/json',
                                        "X-API-Token": apiKey, "Content-Type": "application/json"})
    formatResponse(resp, 'delete dice with wrong id')


def deleteDeviceNoToken():
    resp = delete_device(baseURL, '1', {'accept': 'application/json',
                                        "Content-Type": "application/json"})
    formatResponse(resp, 'delete device')
