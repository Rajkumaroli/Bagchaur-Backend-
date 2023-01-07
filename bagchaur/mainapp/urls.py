from django.urls import path
from mainapp.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
    path('introduction/', introduction, name='introduction'),
    path('janpratinidhi/', janpratinidhi, name='janpratinidhi'),
    path('staff/', staff, name='staff'),
    path('ward1/', ward1, name='ward1'),
    path('ward2/', ward2, name='ward2'),
    path('ward3/', ward3, name='ward3'),
    path('ward4/', ward4, name='ward4'),
    path('ward5/', ward5, name='ward5'),
    path('ward6/', ward6, name='ward6'),
    path('ward7/', ward7, name='ward7'),
    path('ward8/', ward8, name='ward8'),
    path('ward9/', ward9, name='ward9'),
    path('ward10/', ward10, name='ward10'),
    path('ward11/', ward11, name='ward11'),
    path('ward12/', ward12, name='ward12'),
    path('municipalD/', municipalD, name='municipalD'),
    path('gazette/', gazette, name='gazette'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)