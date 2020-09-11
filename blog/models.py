from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=222)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title

    # class Meta:
    #     ordering = ('-title',)
