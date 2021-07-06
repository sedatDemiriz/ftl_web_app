from django.urls import path, include
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_jwt.views import obtain_jwt_token
from view_runs import views

urlpatterns = [
    path('api-runs/', views.RunList.as_view()),
    # path('api-runs/<int:pk>/', views.RunListDetail.as_view()),
    path('ann/', include('announcements.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('token-auth/', obtain_jwt_token),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = format_suffix_patterns(urlpatterns)
