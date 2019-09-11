from django.urls import path
from groups.views import GroupCreateView,GroupDetailView,GroupListView

app_name = "groups"

urlpatterns = [
    path('', GroupListView.as_view(), name="group_list"),
    path('new/', GroupCreateView.as_view(), name="group_create"),
    path('<slug>/', GroupDetailView.as_view(), name="group_details"),
]
