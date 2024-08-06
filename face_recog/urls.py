from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('detect_face/', views.detect_face, name='detect_face'),
    path('add_student/', views.add_student, name='add_student'),

]
