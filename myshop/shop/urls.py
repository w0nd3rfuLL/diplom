from django.urls import path
from . import views

urlpatterns = [
    path('', views.cloth_list, name='cloth_list'),
    path('(<category_slug>[-\w]+)/', views.cloth_list, name='cloth_list_by_category'),
    path('(<id>\d+)/(<slug>[-\w]+)/', views.cloth_detail, name='cloth_detail'),
    ]
