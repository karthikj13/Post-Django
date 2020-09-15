from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name="list_post"),
    path('user/<str:username>', UserPostListView.as_view(), name="user_post"),
    path('detail/<int:pk>/', PostDetailView.as_view(), name="detail_post"),
    path('new/', PostCreateView.as_view(), name="post_create"),
    path('detail/<int:pk>/update/', PostUpdateView.as_view(), name="post_update"),
    path('detail/<int:pk>/delete/', PostDeleteView.as_view(), name="post_delete"),
    path('about/',views.about, name="about")
]
