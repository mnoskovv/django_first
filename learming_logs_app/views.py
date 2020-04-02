from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404
from django.urls import reverse

from .models import Topic, Entry
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """Домашняя страница приложения Learning log"""
    return render(request, 'learming_logs_app/index.html')

@login_required
def topics(request):
    """displays a list of themes related to user"""
    topics = Topic.objects.filter(owner = request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learming_logs_app/topics.html', context)

@login_required
def topic(request, topic_id):
    """displays all records about single topic"""
    try:
        topic = Topic.objects.get(id=topic_id)
    except:
        raise Http404
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learming_logs_app/topic.html', context)

@login_required
def new_topic(request):
    """Определяет новую тему"""
    if request.method != 'POST':
        # Данные не отправлялисть, создается пустая форма
        form = TopicForm()
    else:
        # Было отправлено что-то через POST, обрабатываем данные
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit = False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learming_logs_app:topics'))

    context = {'form': form}
    return render(request, 'learming_logs_app/new_topic.html', context)

@login_required
def new_entry(request, topic_id):
    """Adds new info by chosen theme"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learming_logs_app:topic', args = [topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'learming_logs_app/new_entry.html', context)

@login_required
def edit_entry(request, entry_id):
    """Allows to edit selected entry"""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = EntryForm(instance = entry)
    else:
        form = EntryForm(instance = entry, data = request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learming_logs_app:topic', args = [topic.id]))
    
    context = {'entry' : entry, 'topic' : topic, 'form' : form}
    return render(request, 'learming_logs_app/edit_entry.html', context)

@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    entry.delete()
    
    return HttpResponseRedirect(reverse('learming_logs_app:topic', args = [topic.id]))

@login_required
def delete_topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)

    topic.delete()

    return HttpResponseRedirect(reverse('learming_logs_app:topics'))

