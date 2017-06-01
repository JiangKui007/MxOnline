# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/5/25 16:39'
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True,min_length=6)



