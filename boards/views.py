from django.shortcuts import render, get_object_or_404
from .models import Board, Topic


# Create your views here.
def index(request):
    boards = Board.objects.all()
    return render(request, 'board_index.html', {'boards': boards})


def board_topics(request, id):
    board = get_object_or_404(Board, id=id)
    return render(request, 'topics.html', {'board': board})
