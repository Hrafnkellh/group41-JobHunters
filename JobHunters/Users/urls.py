from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('/sign_up', views.sign_up_index, name='sign_up_index'),
    path('/log_in', views.log_in_index, name='log_in_index')
]
