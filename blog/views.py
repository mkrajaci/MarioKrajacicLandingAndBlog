from django.shortcuts import render

# Create your views here.

posts = [
    {
       'author': 'Mario',
       'title': 'Blog 1',
       'content': 'Prvi post',
       'date_posted': '07 Rujan, 2019',
    },
    {
       'author': 'Marija',
       'title': 'Blog 2',
       'content': 'Drugi post',
       'date_posted': '08 Rujan, 2019',
    }
]


def blog(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
