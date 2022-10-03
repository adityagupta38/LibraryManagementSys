from django.db import models

# Create your models here.


class User(models.Model):
    username = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=55)


class Books(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='books', editable=False)
    title = models.CharField(max_length=55)
    author = models.CharField(max_length=50)
    description = models.TextField(null=True)

