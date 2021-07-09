from django.urls import path
from .views import*


urlpatterns = [
    path('', Blog.as_view(), name="blog"),
    path('?P<int:id>.+?', blogdetail, name="blog_detail"),
    path('?Psave_comment.+?', save_comment, name="save_comment"),
    path('?P<str:title>.+?', Blogcategory, name="blogcategory"),
]