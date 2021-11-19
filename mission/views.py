from django.shortcuts import render, redirect
from django.contrib import messages
from mission.models import *
from users.models import *
from .forms import *

# mList_view(): 멘티-미션 리스트 확인 뷰
def mList_view(request):
    user = User.objects.get(id=2)
    print(user)
    missions = Mission.objects.filter(userPair=user)
    context = {
        'missions':missions
    }
    return render(request, 'missionList.html', context)


# add_mission_view(): 멘토-미션 추가 뷰
def add_mission_view(request):
    user = User.objects.first()

    if request.method == 'POST':
        new_mission = Mission()
        new_mission.user_nickname = user
        new_mission.userPair = user.pair
        new_mission.title = request.POST['TitleBox']
        new_mission.question = request.POST['contentBox']
        new_mission.save()
        return redirect('mission:mission_list')
    else:
        context = {
            'user':user.nickname,
            'pair':user.pair
        }
        return render(request,'missionPaper.html', context)




