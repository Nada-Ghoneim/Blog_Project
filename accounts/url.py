from django.urls import path , reverse_lazy
from . import  views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/', views.signup, name='signup'),

    path('logout/',auth_views.LogoutView.as_view(),name='logout'),

    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),

    path('change_password/',auth_views.PasswordChangeView.as_view(template_name='chang_password.html'
                                                                  ,success_url=reverse_lazy('login')),name='change_password'),


]