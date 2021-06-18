from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('ann/', views.announcements, name='announcements'),
]