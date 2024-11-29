from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
     path('login/', views.user_login, name='login'),
    path('home/', views.home, name='home'),  # Página de inicio después del login
    path('logout/', LogoutView.as_view(), name='logout'),  # Logout
]