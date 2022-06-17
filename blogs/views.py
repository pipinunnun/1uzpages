from django.shortcuts import render, redirect
from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.http import Http404
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """домашняя страница приложения blogs"""
    return render(request, 'blogs/index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'blogs/topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_addedd')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'blogs/topic.html', context)

@login_required
def new_topic(request):
    """новая тема"""
    if request.method != 'POST':
        # данные не отправились
        form = TopicForm
    else:
        # отправленные данные POST; обработать данные
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            #form.save()
            return redirect('blogs:topics')

    # Вывести пустую или недействительную форму
    context = {'form': form}
    return render(request, 'blogs/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('blogs:topic', topic_id=topic_id)
    context = {'topic': topic, 'form': form}
    return render(request, 'blogs/new_entry.html', context)
@login_required
def edit_entry(request, entry_id):
    """редоктировать существующую запись"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('blogs:topic', topic_id=topic.id)

    context= {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'blogs/edit_entry.html', context)
