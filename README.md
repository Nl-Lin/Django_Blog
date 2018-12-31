# Django_Blog
A simple blog tutorial
博客功能模块暂时只有分类、详情页

view.py
# 博客首页
def index(request):
    posts = Posts.objects.all().order_by('-created_time')
    top_three = Posts.objects.all().order_by('-views')[:3]
    return render(request, 'blog_index.html', locals())

# 文章详情页
def detail(request, article_id):
    post = get_object_or_404(Posts, pk=article_id)
    post.increase_views()
    return render_to_response('blog_detail.html', context={'detail': post})
    
# 博客分类
def category(request, cate_id):  
    #这里的cate_id 必须跟URL.py 里面的 path(r'category/<int:cate_id>/', views.category, name='cate') cate_id一致
    category_list = Category.objects.get(id=cate_id).Get_Posts.all()
    category_name = Category.objects.get(id=cate_id)
    return render(request, 'blog_category.html', locals())

URL.py

app_name = 'Blog'
urlpatterns = [
    path('', views.index, name='index'),
    path(r'detail/<int:article_id>/', views.detail, name='detail'),
    path(r'category/<int:cate_id>/', views.category, name='cate')
]

...我是不是忘记改数据库密码了？？？
