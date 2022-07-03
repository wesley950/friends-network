from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Thread, Comment, Upvote

def index(request):
    recent_threads = Thread.objects.order_by('-pub_date')[:5]
    popular_threads = Thread.objects.annotate(upvotes=Count('upvote')).order_by('-upvotes')[:5]
    return render(request, 'threads/index.html', { 'recent_threads': recent_threads, 'popular_threads': popular_threads })

def detail(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    comments = Comment.objects.filter(thread=thread.id).order_by('-pub_date')
    upvoted = request.user.is_authenticated and Upvote.objects.filter(thread=thread, user=request.user).count() != 0
    return render(request, 'threads/detail.html', { 'thread': thread, 'comments': comments, 'upvoted': upvoted })

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
    upvoted = Upvote.objects.filter(thread=thread, user=request.user).count() != 0
    if not upvoted:
        Upvote.objects.create(thread=thread, user=request.user)
    return HttpResponseRedirect(reverse('threads:detail', args=(thread.id, )))

@login_required
def comment(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    new_comment = Comment(text=request.POST['comment-text'], thread=thread, creator=request.user)
    new_comment.save()
    return HttpResponseRedirect(reverse('threads:detail', args=(thread.id, )))
