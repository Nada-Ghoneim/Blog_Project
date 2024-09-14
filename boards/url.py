from django.urls import path
from . import views
from .views import PostUpdateView

urlpatterns = [
    path('', views.home, name='home'),
    path('blog/<int:blog_id>/new/', views.add_post, name='new post'),
    path('blog/<int:blog_id>/edit_post/<int:post_id>/', PostUpdateView.as_view(), name='edit_post'),
    path('comments/<int:post_id>/', views.add_comment, name='comments'),
]
