from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<slug:slug>/', views.post_detail, name='post_detail'),
    path('register/', views.register, name='register'),
    path('login/',views.CustomLoginView.as_view(), name='login'),
    path('logout/',views.CustomLogoutView.as_view(), name='logout'),
    path('create/', views.create_post, name='create_post'),
]