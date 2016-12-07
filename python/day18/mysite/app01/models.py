from django.db import models

# Create your models here.

import re
from django import forms
from django.core.exceptions import ValidationError


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')  # 将正则表达式编译成对象,方法直接用这个正则去套结果
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class PublishForm(forms.Form):
    user_type_choice = (
        (0, u'普通用户'),
        (1, u'高级用户'),
    )

    user_type = forms.IntegerField(widget=forms.widgets.Select(choices=user_type_choice,
                                                               attrs={'class': "form-control"}))

    title = forms.CharField(max_length=20,
                            min_length=5,
                            error_messages={'required': u'标题不能为空',
                                            'min_length': u'标题最少为5个字符',
                                            'max_length': u'标题最多为20个字符'},
                            widget=forms.TextInput(attrs={'class': "form-control",
                                                          'placeholder': u'标题5-20个字符'}))

    memo = forms.CharField(required=False,
                           max_length=256,
                           widget=forms.widgets.Textarea(
                               attrs={'class': "form-control no-radius", 'placeholder': u'详细描述', 'rows': 3}))

    phone = forms.CharField(validators=[mobile_validate, ],
                            error_messages={'required': u'手机不能为空'},
                            widget=forms.TextInput(attrs={'class': "form-control",
                                                          'placeholder': u'手机号码'}))

    email = forms.EmailField(required=False,
                             error_messages={'required': u'邮箱不能为空', 'invalid': u'邮箱格式错误'},
                             widget=forms.TextInput(attrs={'class': "form-control", 'placeholder': u'邮箱'}))




class UploadFile(models.Model):
    userid = models.CharField(max_length=30)
    file = models.FileField(upload_to='./upload/')
    date = models.DateTimeField(auto_now_add=True)



class UserProfile(models.Model):
    user_info = models.OneToOneField('UserInfo')
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __unicode__(self):
        return self.username


class UserInfo(models.Model):
    user_type_choice = (
        (0, u'普通用户'),
        (1, u'高级用户'),
    )
    user_type = models.IntegerField(choices=user_type_choice)
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    address = models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class UserGroup(models.Model):

    caption = models.CharField(max_length=64)

    user_info = models.ManyToManyField('UserInfo')

    def __unicode__(self):
        return self.caption


class Host(models.Model):
    hostname = models.CharField(max_length=64)
    ip = models.GenericIPAddressField()
    user_group = models.ForeignKey('UserGroup')

    def __unicode__(self):
        return self.hostname