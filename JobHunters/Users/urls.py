from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    #path('/sign_up', views.sign_up_index, name='sign_up_index'),
    #path('/log_in', views.log_in_index, name='log_in_index'),

    path('/sign_up', views.register, name='register'),
    path('/log_in', LoginView.as_view(template_name='Users/log_in.html'), name = 'log_in'),
    path('/log_out', LogoutView.as_view(next_page=None), name='log_out'),
]
