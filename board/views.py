from django.shortcuts import render, redirect
from users.models import *
from .forms import *


# question_view(): 질문 게시판 목록 뷰
def question_view(request):
    user = User.objects.first()

    # if request.method == 'POST':
    #     bNum = request.POST['bNum']
    #     board = Board.objects.get(id=id)
    #     return render(request, 'questionDetail.html', {'board':board})
    boards = Board.objects.all()
    return render(request, 'questionPage.html', {'boards':boards})

# question_detail_view(): 질문 게시판 상세 뷰
def question_detail_view(request, id):
    user = User.objects.first()
    board = Board.objects.get(id=id)
    if request.method == 'GET':
        comments = Comment.objects.filter(c_board=board)
        context = {
            'comments':comments,
            'board':board
        }
        return render(request, 'questionDetail.html', context)


def make_comment_view(request):
    user = User.objects.first()
    #print(bNum)
    bNum = request.POST.get('bID')
    board = Board.objects.get(id=bNum)
    if request.method == 'POST':
        new_comment = Comment()
        new_comment.author = user
        new_comment.content = request.POST['new-comment']
        new_comment.c_board = board
        new_comment.save()
        comments = Comment.objects.filter(c_board=board)
        context = {
            'comments':comments,
            'board':board
        }
        return render(request, 'questionDetail.html', context)
    else:
        comments = Comment.objects.filter(c_board=board)
        context = {
            'comments':comments
        }
        return render(request, 'questionDetail.html', context)


# make_question_view(): 질문 작성 뷰
def make_question_view(request):
    user = User.objects.first()

    if request.method == 'POST':
        new_board = Board()
        new_board.author = user
        new_board.title = request.POST['TitleBox']
        new_board.content = request.POST['contentBox']
        new_board.save()
        return redirect('board:question')
    else:
        return render(request, 'makeQuestion.html')



