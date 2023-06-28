from django.db import models
from django.utils import timezone
from user_api.models import AppUser

# Create your models here.

class PublishedManager(models.Manager):
  def get_queryset(self):
    return super(PublishedManager, self).get_queryset().filter(status='published')
class Post(models.Model):
  STATUS_CHOICES = (
    ('draft', 'Draft'),
    ('published', 'Published'),
  )
  class Status(models.TextChoices):
    DRAFT = 'DRAFT'
    PUBLISHED = 'PUBLISHED'
  title = models.CharField(max_length=250)
  slug = models.SlugField(max_length=250, unique_for_date='publish')
  author = models.ForeignKey(AppUser, related_name='blog_posts', on_delete=models.PROTECT)
  body = models.TextField()
  publish = models.DateTimeField(default=timezone.now)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)
  status = models.CharField(max_length=15, choices=Status.choices, default=Status.DRAFT)
  object = models.Manager() # The default manager.
  published = PublishedManager() # Our custom manager

  class Meta:
    ordering = ('-publish',)

  def __str__(self):
    return self.title
