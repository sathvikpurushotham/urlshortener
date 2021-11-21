from django.http import response
from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Shortner
from .forms import ShortenerForm
# Create your views here.

def index(request):
  context = {}
  context['form'] = ShortenerForm()
  if request.method == 'GET':
    print('run1')
    return render(request, 'index.html', context)
  elif request.method == 'POST':
    used_form = ShortenerForm(request.POST)
    if used_form.is_valid():
      # if Shortner.objects.filter(original_url=shortened_object.original_url).exists()
      shortened_object = used_form.save()
      print(shortened_object.original_url)
      new_url = request.build_absolute_uri('/') + shortened_object.short_url
      original_url = shortened_object.original_url 
      context['new_url']  = new_url
      context['original_url'] = original_url
      print('run2')
      print(used_form)
      return render(request, 'index.html', context)
    
    context['errors'] = used_form.errors
    print('run3',context['errors'])
    return render(request, 'index.html', context)

def redirect(request, s):
  try:
    shortener = Shortner.objects.get(short_url=s)     
    shortener.save()
    return HttpResponseRedirect(shortener.original_url)
  except:
    return HttpResponse('<h1>Snap! This link is not valid.</h1>')