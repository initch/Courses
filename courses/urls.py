from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.index, name='course_index'),
    path('<int:id>/', views.course_details, name='course_details'),
    path('<int:id>/new_board/', views.create_course_board,name='create_course_board')
]
