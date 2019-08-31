from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog, Comment
from .forms import newBlog, CommentForm

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
    blog = get_object_or_404(Blog, pk = pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.blog = blog
            comment.content = form.cleaned_data["content"] 
            comment.save() # 저장
            return redirect("detail", pk) 
    else:
        form = CommentForm()
        return render(request, 'board/detail.html', {'blog': blog, "form":form})

#댓글 수정
def comment_edit(request, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        blog_id = comment.blog.id
        if request.method == "POST":
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                    comment = form.save(commit=False)
                    comment.content = form.cleaned_data["content"]
                    comment.save()
                    return redirect('detail', blog_id)
        else:
            form = CommentForm(instance=comment) 
            return render(request, "board/edit.html", {"form":form})

#댓글 삭제
def comment_delete(request, pk, comment_id):
        comment = get_object_or_404(Comment, id=comment_id)
        blog_id = comment.blog.id 
        comment.delete()
        return redirect('detail', blog_id)