from django.shortcuts import render,get_object_or_404
from .models import Post,Category
import markdown
from comments.forms import CommentForm
# Create your views here.


def index(request):
    post_list = Post.objects.all()
    return render(request, 'blog/blog_index.html', context={
        'post_list': post_list
    })


def archives(request,year,month):
    # Python 中类实例调用属性的方法通常是 created_time.year，
    # 但是由于这里作为函数的参数列表，所以 Django 要求我们把点替换成了两个下划线，即 created_time__year。
    post_list = Post.objects.filter(created_time__year=year, created_time__month=month)
    return render(request, 'blog/blog_index.html', context={
        'post_list': post_list
    })


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate)
    return render(request, 'blog/blog_index.html', context={
        'post_list': post_list
    })


'''
注意这里我们用到了从 django.shortcuts 模块导入的 get_object_or_404 方法，其作用就是当传入的 pk 对应的 Post 在数据库存在时，
就返回对应的 post，如果不存在，就给用户返回一个 404 错误，表明用户请求的文章不存在。
'''


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    '''
    这样我们在模板中展示 {{ post.body }} 的时候，就不再是原始的 Markdown 文本了，
    而是渲染过后的 HTML 文本。注意这里我们给 markdown 渲染函数传递了额外的参数 extensions，
    它是对 Markdown 语法的拓展，这里我们使用了三个拓展，分别是 extra、codehilite、toc。
    extra 本身包含很多拓展，而 codehilite 是语法高亮拓展，这为我们后面的实现代码高亮功能提供基础，
    而 toc 则允许我们自动生成目录（在以后会介绍）。
    '''
    post.body = markdown.markdown(post.body,extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        'markdown.extensions.toc',
    ])

    form = CommentForm()
    comment_list = post.comment_set.all()

    context = {
        'post': post,
        'form': form,
        'comment_list': comment_list,
    }

    return render(request, 'blog/blog_detail.html', context=context)

