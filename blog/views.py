from django.shortcuts import render,get_object_or_404
from .models import Post,Category
import markdown
from comments.forms import CommentForm
# Create your views here.

from django.views.generic import ListView, DetailView


class IndexView(ListView):
    # model。将 model 指定为 Post，告诉 Django 我要获取的模型是 Post。
    model = Post
    # template_name。指定这个视图渲染的模板。
    template_name = 'blog/blog_index.html'
    # context_object_name。指定获取的模型列表数据保存的变量名。这个变量会被传递给模板。
    context_object_name = 'post_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 10


class CategoryView(IndexView):
    # 我们覆写了父类的 get_queryset 方法。该方法默认获取指定模型的全部列表数据。
    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate)


class ArchivesView(IndexView):
    def get_queryset(self):
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        return super(ArchivesView,self).get_queryset().filter(created_time__year=year,created_time__month=month)


# 记得在顶部导入 DetailView
class PostDetailView(DetailView):
    # 这些属性的含义和 ListView 是一样的
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    def get_object(self, queryset=None):
        # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
        post = super(PostDetailView, self).get_object(queryset=None)
        post.body = markdown.markdown(post.body,
                                      extensions=[
                                          'markdown.extensions.extra',
                                          'markdown.extensions.codehilite',
                                          'markdown.extensions.toc',
                                      ])
        return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()
        comment_list = self.object.comment_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


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

    # 阅读量 +1
    post.increase_views()

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

