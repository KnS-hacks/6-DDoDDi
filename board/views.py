from django.shortcuts import render, redirect
from users.models import *
from .forms import *

# question_view(): 질문 게시판 목록 뷰
def question_view(request):
    user = User.objects.first()

    boards = Board.objects.filter(author=user)
    return render(request, 'questionPage.html', {'boards':boards})

# question_detail_view(): 질문 게시판 상세 뷰
def question_detail_view(request):
    user = User.objects.first()
    board = Board.objects.get(author=user)

    if request.method == 'POST':
        # form = CommentForm(request.POST, request.FILES)
        # if form.is_valid():
        #     new_comment = Comment()
        #     new_comment.author = user
        #     new_comment.content = form.cleaned_data['content']
        #     new_comment.board = board
        #     new_comment.save()
        new_comment = Comment()
        new_comment.author = user
        new_comment.content = request.POST['new-comment']
        new_comment.c_board = board
        new_comment.save()
        return redirect('board:question_detail')
    else:
        form = CommentForm()
        comments = Comment.objects.filter(c_board=board)
        print(comments)
        context = {
            'form':form,
            'board':board,
            'comments':comments
        }
        return render(request, 'questionDetail.html', context)

# make_question_view(): 질문 작성 뷰
def make_question_view(request):
    user = User.objects.first()

    if request.method == 'POST':
        form = BoardForm(request.POST, request.FILES)
        if form.is_valid():
            new_board = Board()
            new_board.author = user
            new_board.title = form.cleaned_data['title']
            new_board.content = form.cleaned_data['content']
            new_board.save()
            return redirect('board:question_page')
    else:
        form = BoardForm()
        return render(request, 'makeQuestion.html', {'form':form})



