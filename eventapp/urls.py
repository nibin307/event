from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_load, name='login'),
    path('signup/', views.signup_load, name='signup'),
    path('login_user/', views.sign_in),
    path('signup_user/', views.sign_up),
    path('logout/', views.sign_out),

    path('events/', views.show_events, name='show'),
    path('add/', views.add_event),
    path('detail/<int:id>/', views.detail_event),
    path('edit/<int:id>/', views.edit_event),
    path('delete/<int:id>/', views.delete_event),
]