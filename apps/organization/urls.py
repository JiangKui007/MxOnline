# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/6/11 15:58'

from django.conf.urls import url,include

from .views import OrgView


urlpatterns = [

    # 课程机构首页
    url(r'^list/$', OrgView.as_view(), name="org_list"),


]