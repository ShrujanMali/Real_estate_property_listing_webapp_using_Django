from django.urls import path
from . import views 
from .views import (
    BlogListView,
    BlogUpdateView,
    BlogDetailView,
    BlogDeleteView,
    BlogCreateView,
    SearchResultsView
)

urlpatterns = [
    path('<int:pk>/edit/', BlogUpdateView.as_view(), name='blog_edit'),
    path('<int:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),
    path('new/', BlogCreateView.as_view(), name='blog_new'),
    path('', BlogListView.as_view(), name='blog_list'),
    path('location/', views.location, name='location'), 
    path('search/', SearchResultsView.as_view(), name='search_results'),
]