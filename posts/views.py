from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .forms import PostForm, CommentForm
from .models import Post
from django.core.paginator import Paginator
from django.http import JsonResponse

# Create your views here.
def single_post_view(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    all_posts = Post.objects.exclude(id=post.id).order_by('-created_at')
    comments = post.comments.order_by('-created_at')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = CommentForm()

    # paginator:
    paginator = Paginator(all_posts, 5)
    page_num = request.GET.get("page")
    page_obj = paginator.get_page(page_num)

    return render(request, 'single_post_page.html', {
        'post': post,
        'page_obj': page_obj,
        'comments': comments,
        'form' : form,
    })

@login_required
def create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('stories')
    else:
        form = PostForm()
    return render(request, 'write_only.html', {'form': form})

# post like:
def like_post(request, post_id):
    try:
        post = Post.objects.get(id=post_id)
        post.likes += 1
        post.save()
        return JsonResponse({'likes': post.likes, 'message': 'Liked'})
    except Post.DoesNotExist:
        return JsonResponse({'error': 'Post not found'}, status=404)

