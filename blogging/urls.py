from django.urls import path
from blogging.views import stub_view
#from blogging.views import list_view
from blogging.views import BlogListView
#from blogging.views import detail_view
from blogging.views import BlogDetailView

#path('', stub_view, name="blog_index"),
#path('posts/<int:post_id>/', stub_view, name="blog_detail"),

urlpatterns = [
    path('', BlogListView.as_view(), name="blog_index"),     
    path('posts/<int:pk>/', BlogDetailView.as_view(), name="blog_detail"),
]
