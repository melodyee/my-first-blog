# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm


# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list1.html', {'posts': posts})


def post_detail(request, pk):
    # post = Post.objects.get(pk = pk)
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_month(request, pk):
    # m = int(pk[5:6]) - 1
    # print m
    # date = pk[0:4] + "-" + pk[4:6] + "-" + pk[6:8]
    # print "click month is :" + date
    # date2 = pk[0:4] + "-" + pk[4:5] + str(m) + "-" + pk[6:8]
    # print "click month is :" + date2
    if pk == "August":
        date1 = "2017-09-01"
        date2 = "2017-08-01"
    elif pk == "July":
        date1 = "2017-08-01"
        date2 = "2017-07-01"
    elif pk == "June":
        date1 = "2017-07-01"
        date2 = "2017-06-01"
    elif pk == "May":
        date1 = "2017-06-01"
        date2 = "2017-05-01"
    elif pk == "April":
        date1 = "2017-05-01"
        date2 = "2017-04-01"
    elif pk == "March":
        date1 = "2017-04-01"
        date2 = "2017-03-01"
    elif pk == "February":
        date1 = "2017-03-01"
        date2 = "2017-02-01"
    elif pk == "January":
        date1 = "2017-02-01"
        date2 = "2017-01-01"
    posts = Post.objects.filter(published_date__lte=date1).filter(published_date__gte=date2).order_by('published_date')
    return render(request, 'blog/post_list1.html', {'posts': posts})

