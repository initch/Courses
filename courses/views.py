from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Course
from boards.forms import NewBoardForm
from boards.models import Topic


def index(request):
    courses = Course.objects.all()
    return render(request, 'course_index.html', {'courses': courses})


def course_details(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course_details.html', {'course': course})


def create_course_board(request, id):
    course = get_object_or_404(Course, id=id)
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
            course.board = board
            course.save()
            return redirect('/boards/'+str(board.id)+'/')
    else:
        form = NewBoardForm(initial={'course': course.name})
    return render(request, 'new_board.html', {'form': form})
