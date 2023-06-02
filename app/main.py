from typing import Union
from fastapi import FastAPI
from app.test.test import executeTest

app = FastAPI()

executeTest()
