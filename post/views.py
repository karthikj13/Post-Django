from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Post

class PostListView(ListView):
    model = Post
    template_name = 'post/list_post.html'
    context_object_name = 'all_post'
    ordering = ['-created']
    paginate_by = 3

class UserPostListView(ListView):
    model = Post
    template_name = 'post/user_post.html'
    context_object_name = 'all_post'
    paginate_by = 3

    #modifying the existing query set with new query set to get the objects posted by that particular user
    # by overriding the existing queryset
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username')) #getting username from url
        return Post.objects.filter(author=user).order_by('-created')        #filter the post of that particular user



class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['name','description']

    def form_valid(self, form):                     #Add current user as the author of the Post and save the post
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['name','description']

    def form_valid(self, form):                     #Add current user as the author of the Post
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):                            #Checking whether the current user is the author of the Post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/posts'

    def test_func(self):                            #Checking whether the current user is the author of the Post
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

def about(request):
    
    return render(request, 'post/about.html')



#-----------function view----------------------------------------------
'''
def list_post(request):
    all_post = Post.objects.all()
    context = {"all_post":all_post}

    return render(request, 'post/list_post.html', context)


def detail_post(request, pk):
    post = get_object_or_404(Post, id=pk)
    context = {"post":post}
    
    return render(request, 'post/detail_post.html', context)
'''
#----------------------------------------------------------------------