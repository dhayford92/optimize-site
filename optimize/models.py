from django.urls import reverse
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=250)

    def __str__(self):
        return self.title


class Project(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    field = models.ManyToManyField('Category', related_name='category')
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("detail", kwargs={'pk': self.pk})


class ProjectImage(models.Model):
    image = models.ImageField(upload_to='projects/images')
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    featured = models.BooleanField(default=True)

    def __str__(self):
        return self.project.title + "  |  " + str(self.id)


class Contact(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField()
    number = models.CharField(max_length=250)
    message = models.TextField()

    def __str__(self):
        return self.email


class Team(models.Model):
    image = models.ImageField(upload_to='profile/images')
    name = models.CharField(max_length=250)
    position = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    fb = models.URLField(max_length=300)
    ig = models.URLField(max_length=300)
    tw = models.URLField(max_length=300)
    inl = models.URLField(max_length=300)

    def __str__(self):
        return self.name