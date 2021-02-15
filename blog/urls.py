from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from .views import PostListView, AboutView, SearchView, PostCreateView, PostDetailView, PostUpdateView, PostDeleteView, CategoryCreateView,CategoryListView,PostCategoriesListView,CategoryUpdateView,CategoryDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('about/', AboutView, name='blog-about'),
    path('search/$/', SearchView.as_view(), name='search-bar'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.htm'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.htm'), name='logout'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('category/new/',CategoryCreateView.as_view(),name='category-create'),
    path('categories/',CategoryListView.as_view(),name='blog-categories'),
    path('category/<int:pk>/',PostCategoriesListView.as_view(),name='post-cat'),
    path('category/<int:pk>/update/',CategoryUpdateView.as_view(),name='category-update'),
    path('category/<int:pk>/delete/',CategoryDeleteView.as_view(),name='category-delete'),
]
