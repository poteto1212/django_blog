from django.shortcuts import render

#引数request・・・ユーザーがサーバーにアクセスする時に送られる情報
#renderメソッドがrequestで送られた情報を基にindex.htmlを表示させる
def index(request):
    return render(request,'blogs/index.html')
    