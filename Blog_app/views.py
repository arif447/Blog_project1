from django.shortcuts import render
from django.shortcuts import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from Blog_app.forms import Comment_Form
from django.views.generic import CreateView, ListView, DetailView,\
    View, UpdateView, DeleteView,TemplateView
from Blog_app.models import Blog, Comment, Like
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid
# Create your views here.

class Myblogs(LoginRequiredMixin, TemplateView):
    template_name = 'Blog_app/my_blog.html'


class Blog_list(ListView):
    context_object_name = 'blog'
    model = Blog
    template_name = 'Blog_app/blog_list.html'


class Create_Blog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'Blog_app/create_blog.html'
    fields = ('title', 'content',' blog_image')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        title = blog_obj.title
        blog_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))

@login_required
def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    comment_form = Comment_Form()
    already_liked = Like.objects.filter(blog=blog, user=request.user)
    if already_liked:
        liked = True
    else:
        liked = False

    if request.method == 'POST':
        comment_form = Comment_Form(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return HttpResponseRedirect(reverse('Blog_app:blog_details', kwargs={'slug': slug}))
    return render(request, 'Blog_app/details_blog.html',
                  context={'blog': blog, 'comment_form': comment_form, 'liked': liked})


@login_required
def Liked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    if not already_liked:
        like_post = Like(blog=blog, user=user)
        like_post.save()
    return HttpResponseRedirect(reverse('Blog_app:blog_details', kwargs={'slug': blog.slug}))

@login_required
def Unliked(request, pk):
    blog = Blog.objects.get(pk=pk)
    user = request.user
    already_liked = Like.objects.filter(blog=blog, user=user)
    already_liked.delete()
    return HttpResponseRedirect(reverse('Blog_app:blog_details', kwargs={'slug': blog.slug}))


class update_blogs(LoginRequiredMixin, UpdateView):
    model = Blog
    fields = ('title', 'content',)
    template_name = 'Blog_app/edit_blog.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('Blog_app:blog_details', kwargs={'slug':self.object.slug})


