from django.urls import path 
from . import views


urlpatterns =[
    path('', views.home, name="home"),
    path('project/', views.Project.as_view(), name="project"),
    path('cat/<str:title>', views.category, name="category"),
    path('<int:pk>', views.Detail.as_view(), name="detail"),
    path('contact_quest/', views.contact, name="contact"),
]