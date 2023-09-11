from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='account_login'),
    path('signup/', views.SingUpView.as_view(), name='account_signup'),
    path('<int:pk>/', views.UserView.as_view(), name='account_detail'),
]
