from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    path('sign-up/', views.sign_up, name='sign_up'),
    path('activate/<str:username>', views.activate, name='activate'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
