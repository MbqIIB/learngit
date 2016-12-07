from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    mail = models.CharField(max_length=32)
    qq = models.CharField(max_length=32)
    tel = models.CharField(max_length=32)


class User(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    memo = models.TextField()
    img = models.ImageField()
    user_type = models.ForeignKey("UserType", null=True, blank=True)


class UserType(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


