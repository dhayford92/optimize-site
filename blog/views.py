from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.views.generic import ListView
from .models import*


class Blog(ListView):
    model = Post
    template_name = 'blog.html'
    paginate_by = 8



def blogdetail(request, id):
    post = Post.objects.get(id=id)
    comment = Comment.objects.filter(post_id=post)
    com_count = comment.count()
    context = {## show the deatl of the post 
        'post': post, 
        'comments': comment,
        'com_count': com_count
    }
    return render(request, 'blog-single.html', context)



def save_comment(request):
    if request.method == "POST":
        title = request.POST.get('title')
        email = request.POST.get('email')
        message = request.POST.get('message')
        post = request.POST.get('post')
        post_id = Post.objects.get(id=post)
    ###  try and create the fields in comment 
        comment = Comment(post_id=post_id, title=title, email=email, message=message)
        comment.save()
        return redirect('detail/'+post)
    else:
        return redirect('detail/'+post)



def Blogcategory(request, title):
    posts = Post.objects.filter(category__title__contains=title)
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj
    }
    return render(request, 'blog-category.html', context)