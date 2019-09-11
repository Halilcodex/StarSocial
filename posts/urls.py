from django.urls import path
from posts.views import PostListView,PostCreateView,PostDetailView,PostDeleteView,UserPosts

app_name = "posts"

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('by/<username>', UserPosts.as_view(), name="user_posts"),
    path('new/', PostCreateView.as_view(), name="post_create"),
    path('by/<username>/<int:pk>', PostDetailView.as_view(), name="post_details"),
    path('delete/<int:pk>', PostDeleteView.as_view(), name="post_delete"),
]
