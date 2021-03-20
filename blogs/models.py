from django.db import models

# Create your models here.

#Blogクラスを生成することでBlogs(複数形)のテーブルが自動生成される。
#引数(blamk=False 空欄禁止)　引数(null=Falseデータベースの空欄状態もダメ)

class Blog(models.Model):
    title=models.CharField(blank=False,null=False,max_length=150)
    text=models.TextField(blank=False)
    created_datetime=models.DateTimeField(auto_now_add=True)
    updated_datetime=models.DateTimeField(auto_now=True)
    
    #モデルを表示する時の代表的な値を指定
    #今回titleを指定しているのでBlogモデルを一覧表示した時はtitlカラム内の値で
    #表示される。
    def __str__(self):
        return self.title
        
        