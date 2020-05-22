from django.shortcuts import render,get_object_or_404,redirect
from blog_app.models import BlogPost,Comment
from blog_app.forms import PostForm,CommentForm

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView

# Create your views here.

class AboutView(TemplateView):
    template_name='blog_app/about.html'


class PostListView(ListView):
    context_object_name='post_list'
    model=BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')


class PostDetailView(DetailView):
    context_object_name='post_details'
    model=BlogPost
    def get_success_url(self):
        return reverse_lazy('detailview', kwargs={'pk': self.object.pk})



class CreatePostView(LoginRequiredMixin,CreateView):
    login_url='/login/'
    form_class=PostForm
    model=BlogPost
    def get_success_url(self):
        return reverse_lazy('detailview', kwargs={'pk': self.object.pk})

class UpdatePostView(LoginRequiredMixin,UpdateView):
    login_url='/login/'
    form_class=PostForm
    model=BlogPost
    def get_success_url(self):
        return reverse_lazy('detailview', kwargs={'pk': self.object.pk})


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model=BlogPost
    success_url=reverse_lazy('postlist')


class DraftListView(LoginRequiredMixin,ListView):
    template_name='blog_app/blogpost_draft_list.html'
    context_object_name="drafts"
    login_url='/login/'
    model=BlogPost

    def get_queryset(self):
        return BlogPost.objects.filter(published_date__isnull=True).order_by('created_date')
    def get_success_url(self):
        return reverse_lazy('detailview', kwargs={'pk': self.object.pk})






###############################
@login_required
def add_comment_post(request,pk):
    post=get_object_or_404(BlogPost,pk=pk)

    if request.method =='POST':
         form=CommentForm(request.POST)

         if form.is_valid():
             comment=form.save(commit=False)
             comment.post=post
             comment.save()
             return redirect('detailview',pk=post.pk)


    else:
        form=CommentForm()
    return render(request,'blog_app/comment_form.html',{'form':form})

@login_required
def comment_approve(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    comment.approve()
    return redirect('detailview',pk=comment.post.pk)


@login_required
def comment_remove(request,pk):
    comment=get_object_or_404(Comment,pk=pk)
    post_pk=comment.post.pk
    comment.delete()
    return redirect('detailview',pk=post_pk)

@login_required
def post_publish(request,pk):
    post=get_object_or_404(BlogPost,pk=pk)
    post.publish()
    return redirect('detailview',pk=pk)
