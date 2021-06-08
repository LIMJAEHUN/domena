from django.contrib import admin
from django.urls import path
# index는 대문, blog는 게시판
from main.views import index, blog, posting, remove_post

from django.conf.urls.static import static
from django.conf import settings

app_name='main'

urlpatterns = [
    path('',index),
    path('blog/',blog),
    path('admin/', admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path('', index, name='index'),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path('blog/', blog, name='blog'),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path('blog/<int:pk>/',posting, name="posting"),
    path('blog/<int:pk>/remove/', remove_post),


    #url(r'^join/$', views.signup, name='join'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
