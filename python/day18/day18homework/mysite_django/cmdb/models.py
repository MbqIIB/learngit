from django.db import models

# Create your models here.


class UserInfo(models.Model):
    user = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    mail = models.CharField(max_length=32)
    qq = models.CharField(max_length=32)
    tel = models.CharField(max_length=32)


class HostInfo(models.Model):
    host_status_choice = (
        (0, '下线'),
        (1, '上线'),
    )
    nid = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=32)
    address = models.CharField(max_length=32)
    port = models.IntegerField(default=80)
    status = models.CharField(max_length=32)
