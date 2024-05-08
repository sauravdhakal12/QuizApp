from django.shortcuts import render
from django.http import HttpResponse

def home(req):
  return HttpResponse("<h1>Home</h1>")

def post(req):
  return HttpResponse("<h1>Post</h1>")

def post_detail(req):
  return HttpResponse("<h1>Post Detail<h1>")