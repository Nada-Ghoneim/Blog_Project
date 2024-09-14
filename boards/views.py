from django.utils import timezone
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Blog, Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Show all blogs and add a new one

# Show all blogs and add a new one
@login_required
def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')

        # Save the data to the database
        if name and description:
            Blog.objects.create(name=name, description=description)

    # Fetch existing blogs to display
    blogs = Blog.objects.all().order_by('id')
    paginator = Paginator(blogs, 10)
    page = request.GET.get('page', 1)

    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    # Now that `blogs` is a `Page` object, you can calculate the `start_index`
    start_index = (blogs.number - 1) * blogs.paginator.per_page

    return render(request, 'home.html', {'blogs': blogs, 'start_index': start_index})


# Add new post to a specific blog
@login_required
def add_post(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)  # Get the Blog instance
    viewed_key = f'viewed_blog_{blog_id}'
    if not request.session.get(viewed_key, False):
        blog.views += 1
        blog.save()
        request.session[viewed_key] = True

    if request.method == 'POST':
        # blog.views -= 2
        # blog.save()
        # Receive data from the form
        message = request.POST['message']
        user = request.user

        # Save the data
        post = Post.objects.create(
            created_user=user,
            message=message,
            blog=blog,
        )
        return redirect('new post', blog_id=blog.pk)
    posts = blog.posts.all()
    paginator = Paginator(posts, 10)  # Show 10 posts per page
    page = request.GET.get('page', 1)

    try:
        posts_page = paginator.page(page)
    except PageNotAnInteger:
        posts_page = paginator.page(1)
    except EmptyPage:
        posts_page = paginator.page(paginator.num_pages)

    # Calculate start_index for display purposes
    start_index = (posts_page.number - 1) * posts_page.paginator.per_page

    return render(request, 'posts.html', {'blogs': blog,'posts': posts_page,'start_index': start_index})

# Add a new comment to a specific post
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        comment_text = request.POST.get('addComment')
        user = request.user

        # Create a new comment
        Comment.objects.create(
            created_user=user,
            comment=comment_text,
            post=post,
        )
        # Redirect to the same page to see the new comment
        return redirect('comments', post_id=post_id)

    # Fetch comments related to the specific post
    comments = post.comment.all()
    return render(request, 'comment.html', {'post': post, 'comments': comments})

# Update post
@method_decorator(login_required, name='dispatch')
class PostUpdateView(UpdateView):
    model = Post
    fields = ['message']
    template_name = 'edit_post.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_date = timezone.now()
        post.save()
        return redirect('new post', blog_id=post.blog_id)
