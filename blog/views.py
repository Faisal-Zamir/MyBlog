from django.shortcuts import render
from . forms import CommentForm
from django.shortcuts import render, get_object_or_404,redirect
from . models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class PostListView(ListView):
    model = Post
    template_name = 'blog_post/post_list.html'
    context_object_name = 'posts' # posts wohi name hy jo database main nazar aa rahy hy admin dashboard main
    ordering = ['-date_posted']
    paginate_by = 5
    
class UserPostList(ListView):
    model = Post
    template_name =  'blog_post/user_post.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

# class PostDetailsView(DetailView):
#     model = Post

def post_detail(request, pk):
    template_name = "blog/post_detail.html"
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    context ={"post": post,"comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form}
    return render(request,template_name,context)



class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title','content']
    

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
        

