from django.db import models
from users.models import *

# Create your models here.

class Mission(models.Model):
    id = models.AutoField(primary_key=True)
    #user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    mission_title = models.CharField(max_length=100, null=True)
    mission_contents = models.TextField()
    isMission = models.BooleanField(default=False)

# user_id : 로그인된 유저 아이디
# mentee : 로그인된 유저가 멘토일 경우, 멘티정보
#          로그인된 유저가 멘티일 경우, 자신 유저 아이디 값
# montor : 로그인된 유저가 멘토일 경우, 자신 유저 아이디 값
#          로그인된 유저가 멘티일 경우, 멘토 정보
# 미션 답 