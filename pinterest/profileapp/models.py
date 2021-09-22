from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    #유저가 탈되하면 이도 사라짐 -->cascade
    image = models.ImageField(upload_to='profile/', null=True)
    #media root 밑에 profile이라는 경로가 생겨서 이에 저장됨
    nickname = models.CharField(max_length=20, unique=True, null=True)
    #unique 유일한 닉네임을 설정
    message = models.CharField(max_length=100, null=True)




