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

def mission_detail(request, id):
    if request.method == 'POST':
        mission = Mission.objects.get(id=id)
        return render(request, 'missionDetail.html', {'mission':mission})

def submit_mission(request, id):
    mission = Mission.objects.get(id=id)
    user1 = mission.user_nickname
    user2 = User.objects.get(nickname=mission.userPair)
    print(user1)
    print(user2)

    if request.method == 'POST':
        mission.answer = request.POST.get('subFile')
        mission.mission_check = True
        user1.stamp += 1
        user2.stamp += 1
        user1.save()
        user2.save()
        mission.save()
        return redirect('users:letter-create')
    else:
        return render(request, 'missionSubmit.html', {'mission':mission})
        

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




