from django.db import models
from django.contrib.auth.models import User
from django.utils.text import Truncator
# Create your models here.

class Blog(models.Model):
    name = models.CharField(max_length=70 , unique=True)
    description = models.CharField(max_length=150)
    views = models.PositiveIntegerField(default=0)  # to be positave

    #convert object to string
    def __str__(self):
        return self.name
    def get_comments_count(self):
        return Comment.objects.filter(post__blog=self).count()

    def get_last_comment(self):
        return Comment.objects.filter(post__blog=self).order_by('-created_date').first()

class Post(models.Model):
    message = models.TextField(max_length=5000)
    created_date = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(User,related_name='post', on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, related_name='posts', on_delete=models.CASCADE )

    # convert object to string
    def __str__(self):
        truncated_message = Truncator(self.message).chars(30)
        return truncated_message




class Comment(models.Model):
    comment = models.TextField(max_length=600)
    created_date = models.DateTimeField(auto_now_add=True)
    created_user = models.ForeignKey(User,related_name='comment', on_delete=models.CASCADE)
    post = models.ForeignKey(Post,related_name='comment', on_delete=models.CASCADE)
    updated_by = models.ForeignKey(User,null=True,related_name='+', on_delete=models.CASCADE)
    updated_dt= models.DateTimeField(null=True)


    def __str__(self):
        return self.comment
