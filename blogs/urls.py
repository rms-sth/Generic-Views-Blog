from django.urls import path
from . views import *
urlpatterns = [
path('', PostListView.as_view(), name='post_list'),
path('post/detail/<int:pk>', PostDetailView.as_view(), name='post_detail'),
path('create/', PostCreateView.as_view(), name='post_create'),
path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),
path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
path('post/<int:pk>/comment/', CommmentListView.as_view(), name='comment_list'),
path('post/detail/<int:pk>/create/comment', CommentCreateView.as_view(), name='comment_create'),
]