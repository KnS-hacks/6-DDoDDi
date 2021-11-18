from django.db import models
from users.models import User

# < Mission >
# user_nickname : 미션 페이지 접속 유저(멘토) 닉네임(or 멘티)
# user_pair : 유저 멘티들(or 멘토)
# title : 미션 제목
# question : 미션 내용
# answer : 미션 답
# mission_check : 미션 여부

class Mission(models.Model):
    id = models.AutoField(primary_key=True)
    user_nickname = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="user_nickname")  
    userPair = models.CharField(max_length=100, blank=True)
    title = models.CharField(max_length=100, blank=True)
    question = models.TextField()
    answer = models.CharField(max_length=100, blank=True)
    mission_check = models.BooleanField(default=False)

    def __str__(self):
        return self.title

