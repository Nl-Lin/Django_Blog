from django.shortcuts import render, get_object_or_404, render_to_response, HttpResponse
from blog.models import *
from django.db.models import Q

# Create your views here.


# 博客首页
def index(request):
    posts = Posts.objects.all().order_by('-created_time')
    top_three = Posts.objects.all().order_by('-views')[:3]
    # category_list = Category.objects.all()

    return render(request, 'blog_index.html', locals())


# 文章详情页
def detail(request, article_id):
    post = get_object_or_404(Posts, pk=article_id)
    post.increase_views()
    return render_to_response('blog_detail.html', context={'detail': post})


def category(request, cate_id):
    category_list = Category.objects.get(id=cate_id).Get_Posts.all()
    category_name = Category.objects.get(id=cate_id)
    return render(request, 'blog_category.html', locals())





