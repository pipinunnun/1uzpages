"""определяет схемы url для blogs"""
from django.urls import path
from . import views

app_name = 'blogs'
urlpatterns = [
    # home page
    path('', views.index, name='index'),
    # Страница списка тем
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('new_topic/', views.new_topic, name='new_topic'),
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]
