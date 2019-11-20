# snippets/urls.py
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from tasks import views

urlpatterns = [
    path('tasks/', views.TaskList.as_view(), name='task-list'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task-detail'),
    path('tasks/<int:pk>/highlight/',
         views.TaskHighlight.as_view(), name='task-highlight'), # new
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
]


urlpatterns = format_suffix_patterns(urlpatterns)