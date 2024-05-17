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
    
    #path(route='<int:id>/jobApplication/', view=views.JAP_1_1, name='jobApp_1_1'),
    #path(route='<int:id>/jobApplication/', view=views.jobApplicationPage1Contact, name='jobApplication'),
    #path(route='<int:id>/jobApplicationn/', view=views.jobApplicationPage2Cover,  name='jobApplicationn'),
    #path(route='<int:id>/jobApplication3/', view=views.jobApplicatonPage3,  name='jobApplication3')
]
