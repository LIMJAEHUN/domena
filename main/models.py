from django.db import models

# Create your models here.
class Post(models.Model):
    rogophoto = models.ImageField(blank=True, null=True, verbose_name='회사사진')
    postname = models.CharField(max_length=50, verbose_name='제목')
    author = models.CharField(max_length=10, null=True,  verbose_name='작성')
    jop = models.CharField(max_length=50,null=True, verbose_name='직업')
    mainphoto = models.ImageField(blank=True, null=True, verbose_name='사진첨부')
    write = models.TextField(verbose_name='세부내용',null=True,)
    contents = models.TextField(verbose_name='내용')
    created_date = models.DateTimeField(auto_now_add=True, null = True, verbose_name='등록시')

    #user = models.ForeignKey(max_length=10, null=True, verbose_name='작성자',default='')
  # 게시글의 제목(postname)이 Post object 대신하기
    def __str__(self):
        return self.postname
