from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index ),
    path('blast', views.blast),
    path('info', views.info),
]