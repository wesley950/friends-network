from django.urls import path

from . import views

app_name = 'threads'
urlpatterns = [
    path('', view = views.index, name='index'),
    path('t/new/', view = views.new, name='new'),
    path('t/<thread_id>/', view = views.detail, name='detail'),
    path('t/<thread_id>/upvote/', view = views.upvote, name='upvote'),
    path('t/<thread_id>/comment/', view = views.comment, name='comment'),
]