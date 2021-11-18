from django.shortcuts import render,redirect, get_object_or_404
from users import models as usermodel
from .models import Letter
from .forms import LetterForm
# Create your views here.

def home(request):
    return render(request, "startPage.html")


def mypage(request):
    user = get_object_or_404(usermodel.User, pk=1)
    return render(request, "mainPage.html", {'user':user})


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