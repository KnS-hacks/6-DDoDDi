from django.shortcuts import render,redirect, get_object_or_404
from .models import Letter, User
from .forms import LetterForm
# Create your views here.

def home(request):
    return render(request, "startPage.html")


def mypage(request):
    user = get_object_or_404(User, pk=2)
    mentor = get_object_or_404(User, pk=1)
    return render(request, "mainPage.html", {'user':user, 'mentor': mentor})


def letter_list(request):
    letters = Letter.objects.all().order_by('-created_at')
    context = {
        'letters': letters,
    }
    return render(request, 'letterList.html', context)


def letter_create(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            new_item = form.save()
        return redirect('users:letter-list')
    form = LetterForm()
    return render(request,'letterCreate.html', {'form': form})


def letter_delete(request):
    passs


def matching(request):
    if request.method == 'POST':
        mentee = User.objects.get(pk=2)
        mentee.pair = "율희짱"
        mentee.matching_check = True
        mentee.save()

        mentor = User.objects.get(pk=1)
        mentor.pair = "지영짱"
        mentor.matching_check = True
        mentor.save()

        print("====",mentee.nickname, mentee.pair, mentee.matching_check)
        print("====",mentor.nickname, mentor.pair, mentor.matching_check)
        return render(request, 'matching.html', {'mentee': mentee, 'mentor': mentor})

    return redirect('mypage')

