from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='user_index'),
    path('sign_up', views.register, name='register'),
    path('log_in', views.login_page, name='log_in'),
    path('log_out', LogoutView.as_view(next_page = 'log_in'), name='log_out'),
    path('profile', views.profile, name='profile'),
    path(route='employers/<int:id>', view=views.employerDetails, name='employer_details'),
    path(route='profile/<int:id>', view=views.applicationDetails, name='application_details'),
    path('change_user_password', views.change_user_password, name='change_user_password'),
]
