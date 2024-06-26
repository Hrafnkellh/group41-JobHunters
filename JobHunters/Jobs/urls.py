from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('faq', views.faq, name='faq'),
    path('aboutus', views.aboutUs, name='aboutUs'),
    path('jobtips', views.jobTips, name='jobTips'),
    path('employers', views.employers, name='employers'),
    path(route='<int:id>', view=views.jobDetails, name='jobDetails'),
    path(route='<int:id>/jobApplication/', view=views.jobApplication, name='job_application'),
]
