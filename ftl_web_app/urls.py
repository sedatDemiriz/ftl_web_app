"""ftl_web_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
# from rest_framework import routers

from view_runs import views

# router = routers.DefaultRouter()
# router.register(r'api-runs', RunViewSet, basename='run')

urlpatterns = [
    # path('', include(router.urls)),
    path('api-runs/', views.RunList.as_view()),
    path('api-runs/<int:pk>/', views.RunListDetail.as_view()),
    # path('api-runs/<int:pk>/', views.get_post_runs),
    path('ann/', include('announcements.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
