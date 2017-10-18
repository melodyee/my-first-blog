# -*- coding: utf-8 -*-
# __author__ = 'libingxin'

# from django.http import HttpResponse
#
#
# def hello(request):
#     return HttpResponse("Hello World !")

from django.shortcuts import render


def hello(request):
    context = {}
    context["hello"] = "Hello World !!!"
    context["Melody"] = "I AM Melody!!!"

    return render(request, 'hello.html', context)


def bootstrap(request):
    return render(request, 'melody/testBootstrapbasic.html')


def bootstrapform(request):
    return render(request, 'melody/testBootstrapform.html')


def bootstrapdemo(request):
    return render(request, 'melody/testBootstrapdemo.html')

