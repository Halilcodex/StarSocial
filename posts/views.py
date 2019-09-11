from django.shortcuts import render
from posts.models import Post
from django.views.generic import TemplateView,ListView,CreateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.http import Http404
from django.contrib import messages
from django.core.paginator import Paginator

# Using Select Related Mixins: This is a kind of performance booster, in the sense that the database only has to be hit once for a queryset with connections to a foreignkey
# Then subsequent hits will be on the already called query set since the table would have been prepopulated from the initial call
from braces.views import SelectRelatedMixin

# Instatiating the user for the current session
User = get_user_model()

# Create your views here.
class PostListView(SelectRelatedMixin, ListView):
    model = Post
    template_name = "posts/post_list.html"
    select_related = ('user', 'group')
    paginate_by = 3
    queryset = Post.objects.all()


class UserPosts(LoginRequiredMixin, SelectRelatedMixin, ListView):
    model = Post
    template_name = "posts/user_posts_list.html"
    paginate_by = 2
    queryset = Post.objects.all()

    def get_queryset(self):
        try:
            self.user_post = User.objects.prefetch_related("posts_by_user").get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.user_post.posts_by_user.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_post"] = self.user_post 
        return context
    

class PostDetailView(SelectRelatedMixin, DetailView):
    model = Post
    template_name = "posts/post_details.html"
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset =  super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))
    

class PostCreateView(CreateView, SelectRelatedMixin, LoginRequiredMixin):
    model = Post
    fields = ('group', 'post_text')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class PostDeleteView(DeleteView,SelectRelatedMixin, LoginRequiredMixin):
    model = Post
    success_url = reverse_lazy('posts:post_list')
    select_related = ('user', 'group')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "POST DELETED")
        return super().delete(request, *args, **kwargs)
    

