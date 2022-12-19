from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('add', views.add, name='add'),
    path('success', views.success, name='success'),
    path("accounts/register", views.register, name="register")
]