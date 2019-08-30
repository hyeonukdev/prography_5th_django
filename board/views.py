from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import newBlog

#메인
def welcome(request):
    return render(request, 'board/index.html')

#포스트글 보기
def read(request):
    blogs = Blog.objects.all()
    #pagination 구현
    paginator = Paginator(blogs,6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'board/read.html',{'blogs':blogs,'posts':posts})

#포스트 생성
def create(request):
    if request.method == 'POST':
        form = newBlog(request.POST)
        if form.is_valid:
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = newBlog()
        return render(request, 'board/new.html', {'form':form})

#포스트 수정
def update(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    form = newBlog(request.POST, instance = blog) #pk에 해당하는 입력공간을 가져옴
    
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'board/new.html', {'form':form})

#포스트 삭제
def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

#포스트 자세히
def detail(request, pk):
    blog_detail = get_object_or_404(Blog, pk = pk)
    return render(request, 'board/detail.html', {'blog': blog_detail})