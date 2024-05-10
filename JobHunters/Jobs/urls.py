from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('faq', views.faq, name='faq'),
    path('aboutus', views.aboutUs, name='aboutUs'),
    path('jobtips', views.jobTips, name='jobTips'),
    path('employers', views.employers, name='employers'),
]
