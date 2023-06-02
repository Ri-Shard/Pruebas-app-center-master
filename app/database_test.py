import requests
import pytest
from app.database import get_collection

collection = get_collection()
headers = collection.find_one()["headers"]
invalid = collection.find_one()["invalid"]
userID = "15605805-f24b-42d9-9e0c-6af1f8b243b1"
invalidUserID = "15605805-f24b-42d9-9e0c-6af1f8b243"
##CASO PRUEBA 1 ##INFORMACION DEL USUARIO TOKEN VALIDO
def test_get_user_verify_email():
    url = f"https://api.appcenter.ms/v0.1/user"

    response = requests.get(url, headers=headers)
    data = response.json()

    expected = collection.find_one()["prueba_1"]["expected"]
    assert data["email"] == expected

##CASO PRUEBA 2 ##INFORMACION DEL USUARIO TOKEN INVALIDO
def test_get_user_invalid_token():
    url = f"https://api.appcenter.ms/v0.1/user"

    response = requests.get(url, headers=invalid)
    data = response.json()

    expected = collection.find_one()["prueba_2"]["expected"]
    assert data["code"] == expected

##CASO PRUEBA 3 ##INICIO SESION USUARIO SIN TOKEN

def test_get_user_no_token():
    url = f"https://api.appcenter.ms/v0.1/user"

    response = requests.get(url)
    data = response.json()

    expected = collection.find_one()["prueba_3"]["expected"]
    assert data["code"] == expected

##CASO PRUEBA 4 ## REGISTRO EXITOSO DE DISPOSITIVO

def test_create_device_success():
    url = f"https://api.appcenter.ms/v0.1/users/{userID}/devices/register"

    payload = collection.find_one()["prueba_4"]["payload"]
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    expected = collection.find_one()["prueba_4"]["expected"]
    assert data["model"] == expected

##CASO PRUEBA 5 ## REGISTRO DISPOSITIVO SIN DATOS

def test_create_device_void_body():
    url = f"https://api.appcenter.ms/v0.1/users/{userID}/devices/register"

    payload = collection.find_one()["prueba_5"]["payload"]
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    expected = collection.find_one()["prueba_5"]["expected"]
    assert data["message"] == expected

##CASO PRUEBA 6 ## REGISTRO DISPOSITIVO WRONG ID USER

def test_create_device_wrong_if_user():
    url = f"https://api.appcenter.ms/v0.1/users/{invalidUserID}/devices/register"

    payload = collection.find_one()["prueba_6"]["payload"]
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    expected = collection.find_one()["prueba_6"]["expected"]
    assert data["message"] == expected

##CASO PRUEBA 7 ##OBTENER LISTA DISPOSITIVOS USUARIO CON TOKEN VALIDO

def test_get_user_devices():
    url = f"https://api.appcenter.ms/v0.1/user/devices"

    response = requests.get(url,headers=headers)
    data = response.json()

    expected = collection.find_one()["prueba_7"]["expected"]
    assert data[0]["udid"] == expected

##CASO PRUEBA 8 ##OBTENER LISTA DISPOSITIVOS USUARIO CON TOKEN INVALIDO

def test_get_user_devices_invalid_token():
    url = f"https://api.appcenter.ms/v0.1/user/devices"

    response = requests.get(url,headers=invalid)
    data = response.json()

    expected = collection.find_one()["prueba_8"]["expected"]
    assert data["code"] == expected

##CASO PRUEBA 9 ##OBTENER LISTA DISPOSITIVOS USUARIO SIN TOKEN

def test_get_user_devices_no_token():
    url = f"https://api.appcenter.ms/v0.1/user/devices"

    response = requests.get(url)
    data = response.json()

    expected = collection.find_one()["prueba_9"]["expected"]
    assert data["statusCode"] == expected

##CASO PRUEBA 10 ##OBTENER LISTA INFORMACION DE UN DISPOSITIVO ESPECIFICO DE UN USUARIO

def test_get_user_devices_specified_user():
    url = f"https://api.appcenter.ms/v0.1/user/devices/1"

    response = requests.get(url,headers=headers)
    data = response.json()

    expected = collection.find_one()["prueba_10"]["expected"]
    assert data["model"] == expected

##CASO PRUEBA 11 ##OBTENER LISTA INFORMACION DE UN DISPOSITIVO ESPECIFICO DE UN USUARIO TOKEN INVALIDO

def test_get_user_devices_specified_user_invalid_token():
    url = f"https://api.appcenter.ms/v0.1/user/devices/1"

    response = requests.get(url,headers=invalid)
    data = response.json()

    expected = collection.find_one()["prueba_11"]["expected"]
    assert data["code"] == expected

##CASO PRUEBA 12 ##OBTENER LISTA INFORMACION DE UN DISPOSITIVO QUE NO EXISTE

def test_get_user_unexist_devices():
    url = f"https://api.appcenter.ms/v0.1/user/devices/2"

    response = requests.get(url,headers=headers)
    data = response.json()

    expected = collection.find_one()["prueba_12"]["expected"]
    assert data["code"] == expected
##CASO PRUEBA 13 ##ELIMINAR UN DISPOSITIVO
def delete_device():
    url = f"https://api.appcenter.ms/v0.1/user/devices/1"
    response = requests.delete(url, headers=headers)
    data = response.json()
    expected = collection.find_one()["prueba_13"]["expected"]

    assert data == expected

##CASO PRUEBA 14 ##ELIMINAR UN DISPOSITIVO TOKEN INVALIDO
def delete_device_Invalid():
    url = f"https://api.appcenter.ms/v0.1/user/devices/1"
    response = requests.delete(url, headers=invalid)
    data = response.json()
    expected = collection.find_one()["prueba_14"]["expected"]
    assert data["code"] == expected

##CASO PRUEBA 15 ##ELIMINAR UN DISPOSITIVO NO REGISTRADO
def delete_device_not_Registered():
    url = f"https://api.appcenter.ms/v0.1/user/devices/1"
    response = requests.delete(url, headers=invalid)
    data = response.json()
    expected = collection.find_one()["prueba_15"]["expected"]
    assert data["code"] == expected 