from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register),
    path('create/', views.create_line),
    path('line/<int:id>/update/', views.update_line),
    path('line/<int:id>/delete/', views.delete_line),
    path('line/', views.list_lines),
]