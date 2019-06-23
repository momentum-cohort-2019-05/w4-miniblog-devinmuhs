from django.shortcuts import render
from django.views import generic

# Create your views here.

from blog.models import BlogPost, Blogger, Comment

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_blogs = BlogPost.objects.all().count()
    num_comments = Comment.objects.all().count()
    
    # The 'all()' is implied by default.    
    num_bloggers = Blogger.objects.count()
    
    context = {
        'num_blogs': num_blogs,
        'num_comments': num_comments,
        'num_bloggers': num_bloggers,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)



class BlogPostListView(generic.ListView):
    model = BlogPost
    paginate_by = 5

class BlogPostDetailView(generic.DetailView):
    model = BlogPost

class BloggerListView(generic.ListView):
    model = Blogger
    
class BloggerDetailView(generic.DetailView):
    model = Blogger