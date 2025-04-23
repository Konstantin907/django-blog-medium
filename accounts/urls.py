from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/<int:user_id>', views.profile_page_view, name='profile_page'),
    path('profile/<int:user_id>/texts/', views.profile_texts, name='texts'),
    path('profile/<int:user_id>/about/', views.profile_about, name='about'),
    path('profile/<int:user_id>/upload-image/', views.upload_profile_image, name='upload_profile_image'),
]
