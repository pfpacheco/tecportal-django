# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
import base64
import os


BLOCK_SIZE = 16
PADDING = '{'


pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * PADDING


EncodeAES = lambda c, s: base64.b64encode(c.encrypt(pad(s)))


DecodeAES = lambda c, e: c.decrypt(base64.b64decode(e)).rstrip(PADDING)


secret = os.urandom(BLOCK_SIZE)


def encode(data):
    cipher = AES.new(secret)
    return EncodeAES(cipher, data)


def decode(data):
    cipher = AES.new(secret)
    return DecodeAES(cipher, data)
