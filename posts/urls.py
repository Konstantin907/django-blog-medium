from django.urls import path
from . import views

urlpatterns = [
    path('single_post/<int:post_id>/', views.single_post_view, name='post_detail'),
    path('create_post/', views.create_view, name='create_post'),
    path('like/<int:post_id>/', views.like_post, name='like_post')
]
