from math import sqrt,pi

print(sqrt(16))
print(pi)

# need to create __init__.py file inorder to create package

from packages.maths import *

print(addition(5,10))

import os

print(os.getcwd())

import shutil

shutil.copyfile("test.txt","destination.txt")

import json

data = {"name":"Dipanjan","age":38}

json_str = json.dumps(data)
print(type(json_str))

parsed_str = json.loads(json_str)
print(type(parsed_str))

from datetime import datetime,timedelta

print(datetime.now())
print(datetime.now() - timedelta(days=1))

import time

print(time.time())
print(time.sleep(5))
print(time.time())