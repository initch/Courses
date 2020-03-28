from django.urls import path
from . import views

app_name = 'boards'
urlpatterns = [
    path('', views.index, name='board_index'),
    path('new/',views.new_board, name='new_board'),
    path('<int:id>/', views.board_topics, name='topics'),
    path('<int:id>/new/',views.new_topic,name='new_topic'),
    path('<int:id>/topics/<int:topic_id>/',views.topic_posts, name='topic_posts')
]
