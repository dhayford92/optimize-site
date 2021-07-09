from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView
from .models import*
from .models import Project as ProjectModel
from blog.models import Post
from django.core.paginator import Paginator


def home(request):
    teams = Team.objects.all()
    posts = Post.objects.all().order_by('-id')
    proj = ProjectModel.objects.all().order_by('-id')
    context = {
        'teams': teams, 'projects': proj, 'posts': posts
    }
    return render(request, 'index.html', context)


class Detail(DetailView):
    model = Project
    template_name =  "project-detail.html"


class Project(ListView):
    model = Project
    paginate_by = 3
    template_name =  "project.html"



def category(request, title):
    posts = ProjectModel.objects.filter(field__title__contains=title)
    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'posts': posts,
        'page_obj': page_obj,
    }
    return render(request, "category.html", context)




def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        number = request.POST.get('number')
        message = request.POST.get('message')
        msg = Contact(name=name, email=email, number=number, message=message)
        msg.save()
        messages.success(request, 'Message sent')
        return redirect('/')
    else:
        messages.error(request, 'Error contacting Optimize, please recheck the form')
        return redirect('/')