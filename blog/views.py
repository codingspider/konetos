from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Blog
# Create your views here.
from django.views import View


class BlogListView(View):
    def get(self,request):
        blogs = Blog.objects.filter(created_by_id=request.user.id)
        context = {
            'blogs': blogs
        }
        return render(request, 'blog/list.html',context)


class BlogCreateView(View):
    form = BlogForm()

    def get(self,request):
        context = {
            'form': self.form
        }
        return render(request, 'blog/create.html', context)

    def post(self, request):
        if request.method == 'POST':
            title = request.POST.get('title')
            description = request.POST.get('description')
            short_description = request.POST.get('short_description')
            slug = title.replace(' ', '-')
            slug = slug.lower()
            thumbnail = None

            if request.FILES.get('thumbnail'):
                thumbnail = request.FILES['thumbnail']

            data = Blog(title=title, description=description,short_description=short_description, slug=slug, thumbnail=thumbnail, created_by=request.user, likes=0, visit=0)
            data.save()

        return redirect('blog:blog-list')


class BlogReadView(View):
    def get(self, request, pk):
        counter = Blog.objects.get(pk=pk)
        counter.visit = int(counter.visit) + 1
        counter.save()
        data = Blog.objects.get(pk=pk)
        context = {
            'data': data
        }
        return render(request, 'blog/details.html', context)
