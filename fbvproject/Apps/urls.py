from django.urls import path
from .import views 

urlpatterns = [
    path('courselist', views.courseListView, name='home'),
    path('courselist/<int:pk>/', views.courseDateiView, name='home'),

]
