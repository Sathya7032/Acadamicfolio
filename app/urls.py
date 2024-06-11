from django.urls import path
from .views import *

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('test/', testEndPoint, name='test'),
    path('', getRoutes),
    
    path("todo/<user_id>/", TodoListView.as_view()),
    path("todo-detail/<user_id>/<todo_id>/", TodoDetailView.as_view()),
    path("todo-mark-as-completed/<user_id>/<todo_id>/", TodoMarkAsCompleted.as_view()),
    path('todos/<int:user_id>/summary/', TodoSummaryView.as_view(), name='todo_summary'),
    
    path('blogs/', BlogList.as_view(), name='blog-list'),
    path("blogs/<int:blog_id>/",BlogView.as_view(), name='blog'),
    path("blog/<user_id>/", BlogsUserListView.as_view()),
    path("blog/<user_id>/<blog_id>/", BlogsDetailView.as_view()),
    path('blogs/<int:blog_id>/comments/', get_blog_comments, name='get_blog_comments'),
    path('post-blog/', BlogPostCreateView.as_view(), name='post-blog'),
    path('blog/<int:blog_id>/comment/create/', CommentCreateView.as_view(), name='comment_create'),
    
    path('languages/', LanguageList.as_view(), name='languages-list'),
    path('languages/<int:pk>/topics/', TopicsView.as_view(), name='topics-details'),
    path('languages/<int:pk>/codes/', CodeView.as_view(), name='code-details'),
    path('languages/codes/<int:pk>/', CodeDetail.as_view(), name='code-detailsview'),
    
    path('tutorials/', TutorialList.as_view(), name='Tutorials-list'),
    path('tutorials/<int:pk>/', TutorialDetail.as_view(), name='tutorial-detail'),
    path('tutorials/<int:pk>/posts', PostView.as_view(), name='post-details'),
    path('tutorials/<int:post_id>/comments/', get_post_comments, name='get_blog_comments1'),
    path('tutorials/posts/<int:pk>/', PostDetail.as_view(), name='post-detailsview'),
    path('tutorials/<int:post_id>/comment/create/', TutorialCommentCreateView.as_view(), name='comment_create1'),
    
    path('post-problem/', ProblemPostCreateView.as_view(), name='problem-blog'),
    
    path('search/', search_blog, name='search_model'),
    path('search_code/',search_code, name='search_model'),
    path('api/shorts/', ShortListCreateView.as_view(), name='shorts-list-create'),
]