from django.shortcuts import render
from .models import Blog

#引数request・・・ユーザーがサーバーにアクセスする時に送られる情報
#renderメソッドがrequestで送られた情報を基にindex.htmlを表示させる


#クエリセットobjects.order_by()では引数え指定したカラムの値を基準に並べ替える。

def index(request):
    blogs=Blog.objects.order_by('created_datetime')
    return render(request,'blogs/index.html',{'blogs':blogs})
    
#render(,,{'':})の{'',}部分の引数は{'キー'：HTMLに渡す変数}
#pythonの辞書型文法のルールに従って書くこと