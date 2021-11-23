# -*- coding: utf-8 -*-
"""SHA256.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13126o6_8fVC5w6GwgGwkwBir2nt7r4w6
"""



import hashlib, binascii

sha256hash = hashlib.sha256(b'ratibhan').digest()
print("SHA-256('ratibhan') = ", binascii.hexlify(sha256hash))