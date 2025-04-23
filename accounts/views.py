from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import get_object_or_404
from .models import UserProfile
from posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_protect
def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return redirect('register')
        
        user = User.objects.create(username=username, email=email)
        user.set_password(password)
        user.save()

        login(request, user)
        return redirect('stories')
    return render(request, 'register.html')

# login
@csrf_protect
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('stories')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('homepage')
    return redirect('homepage')

#logout:
def logout_view(request):
    logout(request)
    return redirect('homepage')

# here for saving posts:
def profile_page_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    UserProfile.objects.get_or_create(user=user)
    return redirect('texts', user_id=user.id)


def profile_texts(request, user_id):
    user = get_object_or_404(User, id = user_id)
    user_profile, created = UserProfile.objects.get_or_create(user=user)
    user_posts = Post.objects.filter(author = user).order_by('-created_at')

    return render(request, 'profile_page.html', {
        'profile_user': user,
        'user_profile': user_profile,
        'posts': user_posts,
        'active_tab':  'texts',
    })

@login_required
def profile_about(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST' and request.user.id == user.id:
        about_text = request.POST.get('about')
        if about_text:
            user_profile.about = about_text
            user_profile.save()
        return redirect('about', user_id=user.id)

    return render(request, 'profile_page.html', {
        'profile_user': user,
        'user_profile': user_profile,
        'active_tab': 'about',
        'edit_mode': request.GET.get('edit') == '1',
    })

# profile picture upload:
@login_required
def upload_profile_image(request, user_id):
    if request.method == 'POST' and request.user.id == user_id:
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        if 'profile_image' in request.FILES:
            profile.profile_image = request.FILES['profile_image']
            profile.save()
    return redirect('texts', user_id=user_id)
