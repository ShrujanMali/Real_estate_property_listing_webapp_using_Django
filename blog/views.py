from django.contrib.auth.mixins import (
    LoginRequiredMixin, 
    UserPassesTestMixin,
)
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView, View
from django.urls import reverse_lazy
from django.forms import ModelForm
from django.core.serializers.json import DjangoJSONEncoder
from .models import Blog
from django.shortcuts import render
import json
from django.db.models import Q

class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'blog_list.html'
    login_url = 'login'
    queryset = Blog.objects.order_by('-date')

class BlogDetailView(LoginRequiredMixin, DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    login_url = 'login'

class BlogUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Blog
    fields = ('title', 'description', 'email_address', 'want_to')
    template_name = 'blog_edit.html'
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Blog
    template_name = 'blog_delete.html'
    success_url = reverse_lazy('blog_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class BlogCreateView(LoginRequiredMixin, CreateView,ModelForm):
    model = Blog
    template_name = 'blog_new.html'
    fields = ('title', 'description', 'owner', 'address', 'property_type', 'want_to', 'email_address')
    login_url = 'login'


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SearchResultsView(ListView):
    model = Blog
    template_name = 'search_results.html'

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Blog.objects.filter(
            Q(title__icontains=query) | Q(property_type__icontains=query) | Q(want_to__icontains=query) | Q(description__icontains=query) | Q(address__icontains=query)
        )
        return object_list

def location(request): 
    location_list = list(Blog.objects.order_by('title').values()) 
    location_json = json.dumps(list(location_list), cls=DjangoJSONEncoder)  
    context = {'locations': location_json} 
    return render(request, 'location.html', context) 

    