from django.shortcuts import render
from django.http import HttpResponse

def login(req):
  return HttpResponse("<h1>Login</h1>")

def register(req):
  return HttpResponse("<h1>Register</h1>")