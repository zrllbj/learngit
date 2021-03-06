#coding=utf-8
from django.shortcuts import render,render_to_response
from .models import *
from .forms import CommentForm
from django.http import Http404

# Create your views here.
def myBlog(request):
    blog_list=BlogPost.objects.all()
    return render_to_response('BlogTemplate.html',{'blog_list':blog_list})

def get_blogs(request):
    #获得所有的博客按时间排序
    blogs=Blog.objects.all().order_by('-pub')
    #传递context:blog参数
    return render_to_response('blog_list.html',{'blogs':blogs})

def get_details(request,blog_id):
#检查异常
    try:
        #获取固定的blog_id的对象
        blog=Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404
    if request.method == 'GET':
        form = CommentForm()
    else:#请求方法为Post
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data=form.cleaned_data
            cleaned_data['blog']=blog
            Comment.objects.create(**cleaned_data)
    #返回三个参数
    ctx={
        'blog':blog,
        'comments':blog.comment_set.all().order_by('-pub'),
        'form':form
    }
    return render(request,'blog_details.html',ctx)