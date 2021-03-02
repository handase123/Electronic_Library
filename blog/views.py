from django.shortcuts import render,get_object_or_404
from django.db.models import Q
from django.views.generic import ListView, CreateView,DetailView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Post,Category
from django.http import HttpResponse

# Create your views here.

class PostListView(ListView):

    model = Post
    template_name = 'blog/home.htm'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 10
    queryset = Post.objects.all()

class SearchView(ListView):
    model = Post
    template_name = 'blog/search_bar.htm'
    context_object_name = 'posts'
    ordering = '-date_posted'
    paginate_by = 10

    def get_queryset(self):
        if self.request.method == 'GET':
            queries = self.request.GET.get('search')
            if queries:
                queries = queries.split(" ")
                queryset = []
                for q in queries:
                    posts = Post.objects.all().filter(Q(title__icontains=q) | Q(content__icontains=q)).distinct()
                    for post in posts:
                        queryset.append(post)
            else:
                queryset = Post.objects.all()
            return list(set(queryset))


def AboutView(request):
    return render(request, 'blog/about.htm')

class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = Category
    template_name = 'blog/category_form.htm'
    fields = ['category_name']

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CategoryUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    model = Category
    fields = ['category_name']
    template_name = 'blog/category_form.htm'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        category = self.get_object()
        if self.request.user == category.author:
            return True
        return False

class CategoryDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):

    model = Category
    success_url = '/'
    template_name = 'blog/category_confirm_delete.htm'
    context_object_name = 'category'

    def test_func(self):
        category = self.get_object()
        if category.author == self.request.user:
            return True
        return False

class CategoryListView(ListView):

    model = Category
    template_name = 'blog/categories.htm'
    context_object_name = 'categories'
    paginate_by = 10
    queryset = Category.objects.all()

class PostCategoriesListView(ListView):
    model = Post
    template_name = 'blog/post_cat.htm'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        cat_pk = self.kwargs.get('pk')
        posts = Post.objects.all().filter(category_id=cat_pk)
        return posts


class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/post_detail.htm'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin,CreateView):

    model = Post
    fields = ['title','content','book','category']
    template_name = 'blog/post_form.htm'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):

    model = Post
    fields = ['title','content','book','category']
    template_name = 'blog/post_form.htm'

    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):

    model = Post
    success_url = '/'
    template_name = 'blog/post_confirm_delete.htm'
    context_object_name = 'post'

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False
