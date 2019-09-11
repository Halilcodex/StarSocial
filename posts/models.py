from django.db import models
from django.contrib.auth import get_user_model
from groups.models import Group
from django.urls import reverse

# Instantiating the user session
User = get_user_model()

# Create your models here.
class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts_by_user", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name="post_group", on_delete=models.CASCADE, null=True, blank=True)
    post_create_date = models.DateTimeField(auto_now=True)
    post_text = models.TextField(blank=False)

    def save(self,*args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:post_details", kwargs={"username": self.user.username, "pk":self.pk})

    def __str__(self):
        return self.post_text
    
    class Meta:
        ordering=('-post_create_date',)
        unique_together = ['user','post_text']