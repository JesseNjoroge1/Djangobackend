from django.urls import path, re_path
from .views import blog_detail, blog_list

app_name = 'blog'

urlpatterns = [
  re_path('api/posts/', blog_list, name='list'),
  re_path('api/posts/<int:pk>', blog_detail, name='detail'),
]