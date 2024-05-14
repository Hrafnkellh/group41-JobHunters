from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('sign_up', views.register, name='register'),
    path('log_in', LoginView.as_view(template_name='Users/log_in.html'), name = 'log_in'),
    path('log_out', LogoutView.as_view(next_page = 'log_in'), name='log_out'),
    path('profile', views.profile, name='profile'),
    path(route='employers/<int:id>', view=views.employerDetails, name='employer_details')
]
