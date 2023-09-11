from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='account_login'),
    path('signup/', views.SingUpView.as_view(), name='account_signup'),
    path('logout/', views.LogoutView.as_view(), name='account_logout'),
    path('change_password', views.ChangePasswordView.as_view(), name='account_change_password'),
    path('<int:pk>/', views.UserView.as_view(), name='account_detail'),
]
