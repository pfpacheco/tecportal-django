# -*- coding: utf-8 -*-
from django.db import models


class Login(models.Model):

    username = models.CharField(max_length=20, null=False, blank=False)
    password = models.CharField(max_length=10, null=False, blank=False)

    @classmethod
    def get_user_name(cls):
        return cls.username

    @classmethod
    def set_user_name(cls, name):
        cls.username = name

    @classmethod
    def get_password(cls):
        return Login.password

    @classmethod
    def set_password(cls, keyword):
        cls.password = keyword


class ProbeInput(models.Model):

    macAddress = models.CharField(max_length=20, null=False, blank=False)

    @classmethod
    def get_mac_address(cls):
        return ProbeInput.macAddress

    @classmethod
    def set_mac_address(cls, mac_addr):
        cls.macAddress = mac_addr
