# -*- coding: utf-8 -*-
from controllers import auth_user, get_probe_status
from encrypt import encode, decode
from django.shortcuts import render
from django.http import HttpResponseForbidden, Http404


def login(request):
    return render(request, 'login.html')


def index(request):
    if request.method != 'POST':
        raise Exception(HttpResponseForbidden('Only POSTS are allowed to submit data!'))

    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print '-> username = ', username
        print '-> password = ', password
        if username == '' or password == '':
            context = {
                'error_msg': 'Username and Password are required!'
            }
            return render(request, 'login.html', context)
        else:
            ret = auth_user(username, password)
            if 200 == ret.status_code:
                context = {
                    'username': username,
                    'encrypted': encode(password)
                }
                return render(request, 'index.html', context)
            else:
                context = {
                    'error_msg': 'Wrong Username/Password try again!'
                }
                return render(request, 'login.html', context)
    except Exception as expt_msg:
        raise expt_msg


def error(request):
    return render(request, 'error.html')


def result(request):
    if request.method != 'POST':
        raise Http404('Only POSTS are allowed to submit data!')

    try:
        mac_address = request.POST.get('cpe_id')
        username = request.POST.get('username')
        password = decode(request.POST.get('encrypted'))
        if mac_address == '':
            context = {
                'username': username,
                'encrypted': encode(password),
                'error_msg': 'Device CPEID is required!'
            }
            return render(request, 'index.html', context)
        else:
            probe_input = {
                'probeInput': {
                    'macAddress': str(mac_address)
                }
            }
        authentication = (str(username), str(password))
        ret = get_probe_status(probe_input, authentication)
        try:
            context = ret.json().get('probeOutput')
            return render(request, 'result.html', context)
        except:
            context = {
                'username': username,
                'encrypted': encode(password),
                'error_msg': 'Device CPEID informed has not been found!'
            }
            return render(request, 'index.html', context)
    except Exception as expt_msg:
        raise expt_msg

