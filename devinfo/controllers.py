# -*- coding: utf-8 -*-
from json import loads, dumps
from ipware.ip import get_ip
from requests import post, Response
from django.http.response import HttpResponseNotFound


def get_configuration(key):
    configuration = loads(open('/var/www/tecportal/config.json').read())
    return configuration.get(key)


def auth_user(user, password):
    try:
        server = get_configuration('server')
        services = get_configuration('services')
        data = {
            '__ac_name': user,
            '__ac_password': password
        }
        req = post(str(server['url']) + ':' + str(server['port']) + str(services['auth']),
                   data, headers={'content-type':'application/x-www-form-urlencoded; charset = UTF-8'})
    except Exception as expt_msg:
        raise expt_msg
    return req


def get_ip_address(self):
    ip_address = get_ip(self)
    if ip_address is not None:
        return ip_address
    else:
        ip_address = get_ip(self)
    return ip_address


def get_probe_status(probe_input, _auth_):
    try:
        server = get_configuration('server')
        services = get_configuration('services')
        payload = dumps(probe_input)
        req = post(str(server['url']) + ':' + str(server['port']) + str(services['probeStatus']),
                   payload, headers={'content-type': 'application/json'}, auth=_auth_)
    except Exception as expt_msg:
        raise expt_msg
    return req
