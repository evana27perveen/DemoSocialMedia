from django.urls import path
from App_main import views

app_name = 'App_main'

urlpatterns = [
    # path('post-api/', views.PostAPIView.as_view()),
    path('home-post-api/', views.HomePostAPIView.as_view()),
    path('add-new-post-api/', views.AddNewPostAPIView.as_view()),
    path('like-post-api/', views.LikePostAPIView.as_view()),
    path('unlike-post-api/<int:post_id>/', views.unlikeAPIView),
    path('post-comment-api/<int:pk>/', views.CommentViewSet.as_view()),
]
