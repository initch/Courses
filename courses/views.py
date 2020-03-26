from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Course


def index(request):
    courses = Course.objects.all()
    return render(request, 'course_index.html', {'courses': courses})


def course_details(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'course_details.html', {'course': course})
