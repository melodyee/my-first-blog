# -*- coding: utf-8 -*-
# __author__ = 'libingxin'

# from django.http import HttpResponse
# def hello(request):
#     return HttpResponse("Hello World !")

from django.shortcuts import render


def hello(request):
    context = {}
    context["hello"] = "Hello World !!!"
    context["Melody"] = "I AM Melody!!!"

    return render(request, 'hello.html', context)

