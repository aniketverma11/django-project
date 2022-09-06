from django.urls import path
from . import views

urlpatterns = [
    path('', views.exersice, name='exersice' ),
    path('practice2', views.practice, name='practice2'),
]
