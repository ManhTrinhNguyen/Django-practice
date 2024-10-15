from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
  return HttpResponse('Hello World!!!')  

def testing(request):
  path = request.path
  scheme = request.scheme
  method = request.method 

  response = HttpResponse()
  response.headers['Age'] = 26
  
  msg = f'''
  <br>path: {path}
  <br>scheme: {scheme}
  <br>method: {method}
  <br>reponstHeader: {response.headers}
  '''
  return HttpResponse(msg)
