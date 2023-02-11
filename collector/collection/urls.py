from django.urls import path
from django.views.generic import TemplateView

from collection.views import ArchiveView

app_name = 'collection'

urlpatterns = [
    path('', ArchiveView.as_view(), name='index'),
    path('detail/', TemplateView.as_view(template_name='collection/detail.html'), name='detail')
]