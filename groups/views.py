from django.shortcuts import render
from django.views.generic import CreateView,TemplateView,ListView,DetailView
from groups.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

# Create your views here.
class GroupCreateView(CreateView, LoginRequiredMixin):
    model = Group
    fields = ('name', 'description')

class GroupListView(ListView):
    model = Group
    template_name = "groups/group_list.html"
    paginate_by = 3
    queryset = Group.objects.all()

class GroupDetailView(DetailView):
    model = Group
    template_name = "groups/group_details.html"
    context_object_name = 'group_details'
    paginate_by = 2
    queryset = Group.objects.all()

