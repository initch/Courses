from django.shortcuts import render, get_object_or_404, redirect, reverse

from .models import Board, Topic, Post
from .forms import NewBoardForm, NewTopicForm
from courses.models import Course


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
            # course字段不为空就将course和新的board相关联，course存在验证待完善
            if form.cleaned_data.get('course') is not '':
                c = Course.objects.get(name='course')
                c.board = board

            return redirect('/boards/')
    else:
        form = NewBoardForm()
    return render(request, 'new_board.html', {'form': form})


def new_topic(request, id):
    board = get_object_or_404(Board, id=id)
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.save()
            Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
            )
            return redirect(reverse('boards:topic_posts',kwargs={'id':id,'topic_id':topic.id}))  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'new_topic.html', {'board': board, 'form': form})


def topic_posts(request, id, topic_id):
    topic = get_object_or_404(Topic, board__id=id, id=topic_id)
    topic.views += 1
    topic.save()
    return render(request, 'topic_posts.html', {'topic': topic})


