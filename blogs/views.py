from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy, reverse
from .forms import CommentForm


class PostListView(ListView):
    context_object_name = 'posts'
    model = Post


class PostDetailView(DetailView):
	template_name = 'blogs/post_detail.html'
	model = Post

	def get_context_data(self, **kwargs):
	    context = super().get_context_data(**kwargs)
	    context['form'] = CommentForm
	    return context


class PostCreateView(CreateView):
    template_name = 'blogs/post_form.html'
    fields = ('author', 'title', 'content')
    model = Post
    success_url = reverse_lazy('post_list')


class PostUpdateView(UpdateView):
    fields = ('author', 'title', 'content')
    model = Post


class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy("post_list")


class CommmentListView(ListView):
    context_object_name = 'comments'
    model = Comment
    queryset = Comment.objects.get(post)
    print(queryset)


class CommentCreateView(CreateView):
    # template_name = 'blogs/post_detail.html'
    # model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post_id = self.kwargs['pk']
        post = Post.objects.get(id=post_id)
        form.instance.post = post
        return super().form_valid(form)

    def get_success_url(self):
    	post_id = self.kwargs['pk']
    	return reverse('post_detail', kwargs={'pk': post_id})
