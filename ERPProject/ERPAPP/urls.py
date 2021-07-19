from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views

urlpatterns = [
    # path('', views.test, name='home-page'),
    path('', views.Table, name='home-page'),
]

urlpatterns += staticfiles_urlpatterns()