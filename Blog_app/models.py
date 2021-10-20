from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    author = models.ForeignKey(User, related_name='post_author', on_delete=models.CASCADE)
    title = models.CharField(max_length=250, verbose_name='Put the title')
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField(verbose_name='Whats your mind??')
    blog_image = models.ImageField(upload_to='blog_pics', verbose_name='Image')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.title



class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comment_blog', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comment_user', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='comment')
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']
    def __str__(self):
        return self.comment

class Like(models.Model):
    blog = models.ForeignKey(Blog, related_name='liked_post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='liker_user', on_delete=models.CASCADE)

