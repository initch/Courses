from django.urls import path

from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.index, name='course_index'),
    path('<int:id>/', views.course_details, name='course_details')
]
