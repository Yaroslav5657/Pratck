from django.shortcuts import render, redirect
from .forms import PostForm

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Повернення на головну сторінку після успішного створення
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})


# Create your views here.
