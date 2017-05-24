# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/5/24 00:16'

import xadmin


from .models import EmailVerifyRecord
from .models import Banner


class EmailVerifyRecordAdmin(object):
    list_display = ['code','email','send_type','send_time']
    search_fields = ['code','email','send_type','send_time']
    list_filter = ['code','email','send_type','send_time']

class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index','add_time',]
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index','add_time',]


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)