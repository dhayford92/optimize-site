from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blog/images', default='profile/images/default.jpg')
    description = models.TextField()
    category = models.ManyToManyField('Category', related_name='posts', default='uncategorize')
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_on = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blogcategory', args=(str(self.id)))


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Tag(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    link = models.URLField(max_length=250)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    email =  models.CharField(max_length=250)
    message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.title + "   |  " + str(self.post_id)
