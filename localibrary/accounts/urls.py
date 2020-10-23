from django.urls import path 
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    path('register/',views.signup,name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/',views.custom_login_view, name='login'),
    path("lockout/",views.Lockout,name="lockout"),
    path('logout/', auth_views.LogoutView.as_view(template_name='accounts/logout.html'), name='logout'),
]