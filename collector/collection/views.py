from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('collection/collection.html')
    context = {
        'example': 'hello my collection'
    }
    return HttpResponse(template.render(context, request))