from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from posts.models import Post
from django.contrib.auth.models import User
from django.core.paginator import Paginator
 
def homepage(request):
    return render(request, 'base.html')

@login_required(login_url='login')
def stories(request):
    category = request.GET.get('category') #uzima category iz params
    if category:
        posts = Post.objects.filter(category=category).order_by('-created_at')
    else:
        posts = Post.objects.all().order_by('-created_at')
    
    # pagination:
    paginator = Paginator(posts, 6)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    users = User.objects.all()

    return render(request, 'filteringStories.html', 
                  {
                      'posts': posts, 
                      'users': users, 
                      'active_category': category,
                      'page_obj': page_obj,
                   })

