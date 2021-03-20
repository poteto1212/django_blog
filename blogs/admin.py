from django.contrib import admin
from .models import Blog
# Register your models here.

#list_display 一覧表示する際の表示内容
#list_display_links 一覧表示した際の詳細へのリンク指定
class BlogAdmin(admin.ModelAdmin):
    list_display=('id','title','created_datetime','updated_datetime')
    list_display_links=('id','title')


#管理サイトにモデルの操作権限を与えている
admin.site.register(Blog,BlogAdmin)

#インスタンスとはモデルクラスから生成された個々のオブジェクトを指す。
#基本的に一つのインスタンスにつき一つのIDが割り振られる