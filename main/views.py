from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import User, Post, Comment
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
class HomePageView(ListView):
    def get(self, request):
        comments = Comment.objects.all()
        all_posts = Post.objects.all().order_by('-id')
        param = {'posts':all_posts, 'comments': comments}
        return render(request, 'home.html', param)

    def post(self, request):
        user_name = request.POST['uname']
        pwd1 = request.POST['pwd1']
        pwd2 = request.POST['pwd2']
        print(user_name)
        print(pwd1)
        print(pwd2)
        if pwd1 == pwd2:
            add_user = User(username=user_name, password=pwd1)
            add_user.save()
            messages.success(request, 'Account has been created successfully.')
            return redirect('home')
        else:
            messages.warning(request, 'Passwords are not same.')
            return redirect('home')




# Create Upload File System
class UploadView(ListView):
    def get(self, request, user_name):
        return render(request, 'upload_file.html')


    def post(self, request, user_name):
        filename = request.FILES['filename']
        title = request.POST['title']
        desc = request.POST['desc']

        user_obj = User.objects.get(username=user_name)
        upload_post = Post(user=user_obj, title=title, file_field=filename, desc=desc)
        upload_post.save()
        messages.success(request, 'Your Post has been uploaded successfully.')
        return render(request, 'upload_file.html')



# View User Profile
class ProfileView(ListView):
    def get(self, request, user_name):
        user_obj = User.objects.get(username=user_name)
        user_posts = user_obj.post_set.all().order_by('-id')
        param = {'user_data':user_obj, 'user_posts': user_posts}
        return render(request, 'profile.html', param)


# Post Delete View

class DeleteView(ListView):
    model = Post
    def get(self, request, post_id):
        user = request.session['user']
        delete_post = self.model.objects.get(id=post_id)
        delete_post.delete()
        messages.success(request, 'Your post has been deleted successfully.')
        return redirect(f'/profile/{user}')


# Search View
class SearchView(ListView):
    def get(self, request):
        query = request.GET['query']
        search_users = User.objects.filter(username__icontains=query)
        search_title = Post.objects.filter(title__icontains = query)
        search_desc = Post.objects.filter(desc__icontains = query)
        search_result = search_title.union(search_desc)
        param = {'query':query, 'search_result':search_result, 'search_users':search_users}
        return render(request, 'search.html', param)







# Login System
class LoginView(ListView):
    def get(self, request):
        return redirect('home')

    def post(self, request):
        user_name = request.POST['uname']
        pwd = request.POST['pwd']

        user_exists = User.objects.filter(username=user_name, password=pwd).exists()
        if user_exists:
            request.session['user'] = user_name
            messages.success(request, 'You are logged in successfully.')
            return redirect('home')
        else:
            messages.warning(request, 'Invalid Username or Password.')
            return redirect('home')
        return redirect('home')

# Logout System
class LogoutView(ListView):
    def get(self, request):
        try:
            del request.session['user']
        except:
            return redirect('home') 
        return redirect('home')

# Comment System

# class CommentView(ListView):
#     def post(self, request, user_name, file):
#         content = request.POST.get('content')
#         user_obj = get_object_or_404(User, username=user_name)
#         file_obj = get_object_or_404(Post, title=file)
#         comment_post = Comment(comment=content, user=user_obj, post=file_obj)
#         comment_post.save()
#         all_posts = Post.objects.all().order_by('-id')
#         param = {'posts':all_posts}
#         messages.success(request, 'Your Comment has been sent successfully.')
#         return redirect('home', param)
    
#     def get(self,request, user_name, file):
#         return render(request, 'home.html')


def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment')
        user=request.user
        postSno =request.POST.get('postSno')
        post= Post.objects.get(id = postSno)
        comment=Comment(comment= comment, user=user, post=post)
        comment.save()
        comments = Comment.objects.all()
        all_posts = Post.objects.all().order_by('-id')
        param = {'posts':all_posts, 'comments': comments}
        messages.success(request, "Your comment has been posted successfully")
        return render(request, 'home.html', param)
        
    return redirect('home')