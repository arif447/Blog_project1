from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse



def index(request):
    return HttpResponseRedirect(reverse('Blog_app:blog_list'))
