from django.urls import path
from . import views

urlpatterns = [
    path('dash', views.Dashboard, name='dashboard'),
    path('site/', views.SITE, name='site'),
    path('site/add/', views.site_add, name='site_add'),
    path('site/edit/<int:pk>/', views.site_edit, name='site_edit'),
    path('site/delete/<int:pk>/', views.site_delete, name='site_delete'),
]
