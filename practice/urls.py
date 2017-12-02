from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^abc/', views.abc.as_view(), name='abc'),
    url(r'^xyz/', views.xyz.as_view(), name='xyz'),
]
