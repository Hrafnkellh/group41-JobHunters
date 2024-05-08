from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('/sign_up', views.sign_up_index, name='sign_up_index'),
    path('/log_in', views.log_in_index, name='log_in_index'),

    path('/sign_up', views.register, name='Register_User'),
    path('/log_in', LoginView.as_view(template_name='user/log_in.html'), name = 'Log_In_User'),
    path('/log_out', LogoutView.as_view(next_page='log_in'), name='Logout_User'),
]
