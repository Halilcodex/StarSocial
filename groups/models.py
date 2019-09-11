from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from django import template
from django.urls import reverse

# Instantiating the user model to the logged in user in the current session
User = get_user_model()

# Template tagging
register = template.library

# Create your models here.
class Group(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User, through="GroupMember")

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("groups:group_details", kwargs={'slug':self.slug})

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
    

class GroupMember(models.Model):
    group = models.ForeignKey(Group, related_name="memberships", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_groups", on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")
    