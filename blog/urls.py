from django.urls import path
from . import views
from . views import (
    PostListView,
    UserPostList,
    #PostDetailsView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    post_detail

)
urlpatterns = [
    #path('',views.home, name='blog-home'),
    path('',PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostList.as_view(), name='user-post'),
    #path('post/<int:pk>', PostDetailsView.as_view(), name='post-detail')
    path('post/<int:pk>', views.post_detail, name='post-detail'),
    path('post/new', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete')
]