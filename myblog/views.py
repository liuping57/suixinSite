from django.shortcuts import render
from django.views import View
from .models import Blog, Tag, Category, Comment
from pure_pagination import PageNotAnInteger, Paginator, EmptyPage
from myblog.forms import CommentForm
from django.http import HttpResponse


class IndexView(View):
    """
    首页
    """
    def get(self, request):
        blog_list = Blog.objects.all().order_by('-create_time')
        category_list = Category.objects.all()
        tag_list = Tag.objects.all()
        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(blog_list, 5, request=request)  # 5为每页展示的博客数目
        blog_list = p.page(page)

        return render(request, 'index.html',
        {
            'blog_list': blog_list,
            'category_list': category_list,
            'tag_list': tag_list,
        })


class BlogDetailView(View):
    '''
    详情页
    '''
    def get(self,request, blog_id):
        blog = Blog.objects.get(id=blog_id)
        comments_list = Comment.objects.filter(blog__id=blog_id)
        return render(request, 'blog_details.html',
                      {
                          'blog': blog,
                          'comments_list': comments_list,
                      })


class AddCommentView(View):

    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            print(comment_form.errors)
            return HttpResponse('{"status": "fail"}', content_type='application/json')


# class CategoryDetaiView(View):
#
#     def get(self, request, category_name):
#         category = Category.objects.filter(name=category_name).first()
#         cate_blogs = category.blog_set.all()
#
#         # 分页
#         try:
#             page = request.GET.get('page', 1)
#         except PageNotAnInteger:
#             page = 1
#
#         p = Paginator(cate_blogs, 5, request=request)
#         cate_blogs = p.page(page)
#
#         return render(request, 'category-detail.html', {
#             'cate_blogs': cate_blogs,
#             'category_name': category_name,
#         })


# Create your views here.
