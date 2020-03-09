from django.shortcuts import render
#200309追記　https://tutorial.djangogirls.org/ja/dynamic_data_in_templates/
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts':posts})


