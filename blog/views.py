from django.shortcuts import render


def index_view(request):
    return render(request, 'blog/single-blog.html')


def contact_view(request):
    return render(request, 'blog/contact.html')
