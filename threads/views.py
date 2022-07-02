from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Thread, Comment

def index(request):
    recent_threads = Thread.objects.order_by('-pub_date')[:5]
    popular_threads = Thread.objects.order_by('-points')[:5]
    return render(request, 'threads/index.html', { 'recent_threads': recent_threads, 'popular_threads': popular_threads })

def detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    comments = Comment.objects.filter(thread=thread.id).order_by('-pub_date')
    return render(request, 'threads/detail.html', { 'thread': thread, 'comments': comments })

@login_required
def new(request):
    if request.method == 'POST':
        new_thread = Thread(title=request.POST['thread-title'], text=request.POST['thread-text'], creator=request.user)
        new_thread.save()
        return HttpResponseRedirect(reverse('threads:detail', args=(new_thread.id, )))
    return render(request, 'threads/new.html')

@login_required
def upvote(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    thread.points += 1
    thread.save()
    return HttpResponseRedirect(reverse('threads:detail', args=(thread.id, )))

@login_required
def comment(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    new_comment = Comment(text=request.POST['comment-text'], thread=thread, creator=request.user)
    new_comment.save()
    return HttpResponseRedirect(reverse('threads:detail', args=(thread.id, )))
