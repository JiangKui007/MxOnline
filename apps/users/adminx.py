# _*_ coding:utf-8 _*_
__author__ = 'JiangKui'
__date__ = '2017/5/24 00:16'

import xadmin


from .models import EmailVerifyRecord
from .models import Banner
from xadmin import views


class BaseSetting (object):
    enable_themes = True
    use_bootswatch = True


class GlobalSetting(object):
    site_title = "慕学后台"
    site_footer = "云中墨客"
    menu_style = "accordion"


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
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)