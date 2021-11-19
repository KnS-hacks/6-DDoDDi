from django.shortcuts import render, redirect
from django.contrib import messages
from mission.models import *
from users.models import *
from .forms import *

# mList_view(): 멘티-미션 리스트 확인 뷰
def mList_view(request):
    user = User.objects.get(id=2)
    missions = Mission.objects.filter(userPair=user)
    context = {
        'missions':missions
    }
    return render(request, 'missionList.html', context)
    # if request.method == 'POST':
    #     new_answer = request.POST['answer']
    #     mNumber = request.POST['mNumber']
    #     for mission in missions:
    #         if ((int)(mission.id) == (int)(mNumber)):
    #             if (mission.answer == new_answer):
    #                 messages.add_message(request, messages.INFO, '미션 완료!')
    #                 mission.mission_check = True
    #                 mission.save()
    #                 return redirect('mission:mission_list')
    #             else:
    #                 messages.add_message(request, messages.ERROR, '다시 입력해주세요!')
    #                 return render(request, 'missionList.html', context)
    # else:
    #     # missions의 answer 안보이게 처리는 템플릿에서 
    #     return render(request, 'missionList.html', context)

# add_mission_view(): 멘토-미션 추가 뷰
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
            #new_mission.answer = form.cleaned_data['answer']
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




