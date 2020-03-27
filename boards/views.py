from django.shortcuts import render, get_object_or_404, redirect

from .models import Board, Topic
from .forms import NewBoardForm


def index(request):
    boards = Board.objects.all()
    return render(request, 'board_index.html', {'boards': boards})


def board_topics(request, id):
    board = get_object_or_404(Board, id=id)
    return render(request, 'topics.html', {'board': board})


def new_board(request):
    if request.method == 'POST':
        form = NewBoardForm(request.POST)
        if form.is_valid():
            board = form.save()
            board.save()
            if form.cleaned_data.get('topic') is not '':
                Topic.objects.create(
                    subject=form.cleaned_data.get('topic'),
                    board=board
                )
            return redirect('/boards/')
    else:
        form = NewBoardForm()
    return render(request, 'new_board.html', {'form': form})
