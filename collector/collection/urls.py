from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'collection'

urlpatterns = [
    path('', views.index, name='index'),
    path('detail/', TemplateView.as_view(template_name='collection/detail.html'), name='detail')
]