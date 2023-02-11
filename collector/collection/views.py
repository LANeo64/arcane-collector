from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView

from collection.models import Collection

# Create your views here.
class ArchiveView(TemplateView):
    template_name = 'collection/archive.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['collections'] = Collection.objects.all()[:15]
        return context


def archive(request):
    template = loader.get_template('collection/collection.html')
    context = {
        'example': 'hello my collection'
    }
    return HttpResponse(template.render(context, request))