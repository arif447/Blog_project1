from django.urls import path
from Blog_app import views
app_name = 'Blog_app'


urlpatterns = [
    path('blog_list/', views.Blog_list.as_view(), name='blog_list'),
    path('create_blog/', views.Create_Blog.as_view(), name='create_blog'),
    path('details/<slug:slug>', views.blog_details, name='blog_details'),
    path('like/<pk>/', views.Liked, name='like'),
    path('unlike/<pk>/', views.Unliked, name='unlike'),
    path('myblogs/', views.Myblogs.as_view(), name='my_blogs'),
    path('edit/<pk>/', views.update_blogs.as_view(), name='update_blogs'),


]
