from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('', views.frontpage, name='faq'),
    path('', views.frontpage, name='aboutus'),
    path('', views.frontpage, name='jobtips'),
]
