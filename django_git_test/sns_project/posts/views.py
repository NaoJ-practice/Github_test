from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.utils.timezone import now

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(scheduled_date__lte=now(), is_published=True)
    return render(request, 'posts/post_list.html', {'posts':posts})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'posts/post_create.html', {'form': form})