from django.shortcuts import render, redirect
from mission.models import *
from users.models import *
from .forms import *

# mList_view(): 멘티 미션 목록 뷰
def mList_view(request):
    user = User.objects.first()
    missions = Mission.objects.filter(user_nickname=user)
    print(missions)

    return render(request, 'missionList.html', {'missions':missions})

# perform_mission_view(): 멘티 미션 수행 뷰
def perform_mission_view(request):
    user = User.objects.get(id=2)
    missions = Mission.objects.filter(userPair=user.id)

    if request.method == 'POST':
        new_answer = request.POST['answer']
        for mission in missions:
            if (mission.answer == new_answer):
                return redirect('mission:mission_list')
    else:
        # missions의 answer 안보이게 처리는 템플릿에서 
        context = {
            'missions':missions
        }
        return render(request, 'missionList.html', context)

# add_mission_view(): 멘토 미션 추가 뷰
def add_mission_view(request):
    user = User.objects.first()

    if request.method == 'POST':
        form = AddMissionForm(request.POST, request.FILES)
        if form.is_valid():
            new_mission = Mission()
            new_mission.user_nickname = user
            new_mission.userPair = user.pair
            new_mission.title = form.cleaned_data['title']
            new_mission.question = form.cleaned_data['question']
            new_mission.answer = form.cleaned_data['answer']
            new_mission.save()
            return redirect('mission:mission_list')
    else:
        form = AddMissionForm()
        context = {
            'form':form,
            'user':user.nickname,
            'pair':user.pair
        }
        return render(request,'missionPaper.html', context)




