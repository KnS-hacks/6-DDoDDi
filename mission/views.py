from django.shortcuts import render, redirect
from mission.models import *
from users.models import User
from .forms import MissionForm

# Create your views here.

# mission_list_view(): 미션 페이지 뷰
def mission_list_view(request):
    # POST인 경우, 값 처리 
    if request.method == 'POST':
        form = MissionForm(request.POST)
        if MissionForm.is_valid():
            pass
    # POST가 아닌 경우, 화면으로 값 출력
    else:
        user = User.objects.get()
        missions = Mission.objects.filter(user_nickname=user)
        form = MissionForm()
        context = {
            'missionForm': missions
        }

