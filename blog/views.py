from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Author, Categorey
from marketing.models import Signup
from django.db.models import Count, Q
# Create your views here.

def search(request):
    most_recent = Post.objects.order_by('-timestamp')[:3]
    categorey_count = get_categorey_count()
    queryset = Post.objects.all()
    query = request.GET.get('q')
 



    if query:
        queryset = queryset.filter(
            Q(title__icontains=query) 
             
            

        ).distinct()
    
    context = {
        'queryset': queryset,
        'most_recent':most_recent,
        'categorey_count': categorey_count,
        
    }
    return render(request, 'pages/search_result.html', context)

def get_categorey_count():
    queryset = Post.objects.values('categories__title').annotate(Count('categories__title'))
    

    return queryset


def index(request):
    featured = Post.objects.filter(featured=True)
    latest = Post.objects.order_by('-timestamp')[0:3]
    
    if request.method == "POST":
        email = request.POST["email"]
        new_signup = Signup()
        new_signup.email = email
        new_signup.save()
    
    
    context={
        'object_list': featured,
        'latest':latest
    }
    return render(request, 'pages/index.html', context)

def blog(request):
    categorey_count = get_categorey_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post_list = Post.objects.all()

    paginator = Paginator(post_list, 4)
    page_request_var = 'page'
    page = request.GET.get(page_request_var)

    try:
        paginated_queryset = paginator.page(page)
    except PageNotAnInteger:
        paginated_queryset = paginator.page(1)
    except EmptyPage:
        paginated_queryset = paginator.page(paginator.num_pages)

    context = {
        'queryset': paginated_queryset,
        'most_recent': most_recent,
        'page_request_var': page_request_var,
        'categorey_count': categorey_count
    }
    return render(request, 'pages/blog.html', context)


def post(request,id):
    
    categorey_count = get_categorey_count()
    most_recent = Post.objects.order_by('-timestamp')[:3]
    post = get_object_or_404(Post, id=id)
    context ={
        'post': post,
        'most_recent': most_recent,
        'categorey_count': categorey_count
    }
    return render(request, 'pages/post.html', context)


def categorey(request):

    most_recent = Post.objects.order_by('-timestamp')[:3]
    categorey_count = get_categorey_count()
    
    queryset = Post.objects.order_by('categories')
    query = request.GET.get('q')
    if query:
        queryset = queryset.filter(
            Q(title__icontains=query)
        ).distinct()
        
    context ={
        
        'queryset': queryset,
        'most_recent':most_recent,
        'categorey_count': categorey_count
    }
    return render(request, 'pages/categorey.html', context)

# worked for categorey click views to show specific categorey post
