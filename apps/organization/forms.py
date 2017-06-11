# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/11 15:01'

from django import forms

from operation.models import UserAsk



class AnotherUserForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name','mobile','course_name']
