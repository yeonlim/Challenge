from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Community, Comment, Message
from .forms import CommunityForm, CommentForm
from django.core.mail.message import EmailMessage
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponse

def community(request):
    contents = Community.objects.all().order_by('-id')
    paginator = Paginator(contents, 3)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request,'home.html', {'contents' : contents, 'posts' : posts})

def detail(request, id):
    detail_data = get_object_or_404(Community, pk = id)
    comments = Comment.objects.filter(community_id=id, comment_id__isnull=True)

    re_comments = []
    for comment in comments:
        re_comments += list(Comment.objects.filter(comment_id=comment.id))
    
    form = CommentForm()
    return render(request, 'detail.html' ,{'data' : detail_data, 'comments' : comments, 're_comments' : re_comments, 'form':form})

def new(request):
    if request.method == 'POST': #폼 다채우고 저장버튼 눌렀을 때
        form = CommunityForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.writer = request.user
            post.save()
            return redirect('detail', post.id)
        return redirect('home')
    else:  #글을 쓰기위해 들어갔을 때
        form = CommunityForm()
        return render(request,'new.html', {'form':form})


def update(request, id):
    post = get_object_or_404(Community, pk = id)
    if request.method == 'GET':  #수정하려고 들어갔을 때
        form = CommunityForm(instance = post)
        return render(request, 'update.html', {'form' : form})
    else:   #수정 끝나고 수정 버튼을 눌렀을 때
        form = CommunityForm(request.POST, request.FILES, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
            return redirect('/community/detail/' + str(id))
        return redirect('/community')

def delete(request, id):
    delete_data =  Community.objects.get(id = id)
    delete_data.delete()
    return redirect('/community')

def search(request):
    data = Community.objects.all().order_by('-id')

    find = request.POST.get('find', "")

    if find:
        data = data.filter(title__icontains=find)
        return render(request, 'search.html', {'data': data, 'find':find})
    else:
        return render(request, 'search.html')

def create_comment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.community_id = Community.objects.get(pk=id)
            comment.author = request.user
            comment.save()
    return redirect('detail', id)

def create_re_comment(request, id, comment_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.community_id = Community.objects.get(pk=id)
            comment.comment_id = Comment.objects.get(pk=comment_id)
            comment.author = request.user
            comment.save()
    return redirect('detail', id)

def update_comment(request, comment_id, id):
    my_com = Comment.objects.get(id=comment_id)
    com_form = CommentForm(instance=my_com)
    if request.method == "POST":
        update_form = CommentForm(request.POST, instance = my_com)
        if update_form.is_valid():
            update_form.save()
            return redirect('detail', id)
    return render(request, 'detail', {'com_form':com_form})

def delete_comment(request, comment_id, id):
    mycom = Comment.objects.get(id=comment_id)
    mycom.delete()

    return redirect('detail', id)

def email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        data = {
            'name' : name,
            'email' : email,
            'subject' : subject,
            'message' : message
        }
        message = '''
        Username: {} 
        Message: {}
        From: {}
        '''.format(data['name'], data['message'], data['email'])
        send_mail(data['subject'], message, email, ['yolllllim@gmail.com'])
        return HttpResponse('Thank you for sending the mail.')
    return render(request, 'mail.html', {})

def likelion_map(request):
    return render(request, 'map.html')