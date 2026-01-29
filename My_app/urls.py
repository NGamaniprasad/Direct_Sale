from django.urls import path
from . import views

# user name-Ravi
# pwd-Ravi@1234

urlpatterns = [
    path('', views.Flex, name='Flex'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('upload/image/', views.upload_image, name='upload_image'),
    path('upload/video/', views.upload_video, name='upload_video'),
    path('upload/file/', views.upload_file, name='upload_file'),

    path('images/', views.view_images, name='view_images'),
    path('videos/', views.view_videos, name='view_videos'),
    path('files/', views.view_files, name='view_files'),
    path('Media/', views.Media, name='Media'),
    # -8
    path('videos/delete/<int:video_id>/', views.delete_video1, name='delete_video1'),
    path('videos/delete/<int:video_id>/', views.delete_video, name='delete_video'),
    # path('videos/deleted/', views.delete_video1, name='delete_video_success'),
    path('images/delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('images/deleted/', views.delete_image_success, name='delete_image_success'),
    # path('images/delete/<int:image_id>/', views.delete_image, name='delete_image'),
    path('files/delete/<int:file_id>/', views.delete_file, name='delete_file'),
    path('teams/', views.teams, name='teams'),
    path('signup/', views.signup, name='signup'),
    path('user_login/', views.user_login, name='login'),
    path('area/', views.area, name='area'),
    path('products/', views.products, name='products'),
    path('plan/', views.plan, name='plan'),
    path('company', views.company, name='company'),
    path('terms', views.terms, name='terms'),
    path('send-email/', views.send_email, name='send_email'),
    path('send_bulk/', views.send_bulk, name='send_bulk'),

]
