from .models import Article
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login


def archive(request):
    return render(request, 'archives.html', {"posts":Article.objects.all()})


def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404



def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            form = {'text': request.POST["text"], 'title':request.POST["title"]}
            if form["text"] and form["title"]:
                articles = Article.objects.all()
                for article in articles:
                    if article.title == form['title']:
                        form['errors'] = u"Статья с таким названием уже существует"
                        return render(request,'create_post.html',{'form':form})
                Article.objects.create(text=form["text"],title=form["title"], author=request.user)
                return redirect('get_article', article_id = Article.objects.get(title=form['title']).id)
            else:   
                form['errors']   = u"Не все поля заполнены"
                return render(request, 'create_post.html',{'form': form})
        else:
            return render(request, 'create_post.html', {})
    else:
        raise Http404



def create_user(request):
    if request.method == "POST":
        form = {'username': request.POST["username"], 'email': request.POST["email"], 'password':request.POST["password"]}
        if form["username"] and form["email"] and form["password"]:
            users = User.objects.all()
            for user in users:
                if user.username == form['username']:
                    form['errors'] = u"Логин занят"
                    return render(request,'create_user.html',{'form':form})
                if user.email == form['email']:
                    form['errors'] = u"Почта уже используется"
                    return render(request,'create_user.html',{'form':form})
            User.objects.create_user(username=form['username'],email=form['email'],password=form['password'])
            return redirect('site')
        else:   
            form['errors'] = u"Не все поля заполнены"
            return render(request, 'create_user.html',{'form': form})
    else:
        return render(request, 'create_user.html', {})


def authorization(request):
    if request.user.is_anonymous:
        if request.method == "POST":
            form = {'username': request.POST["username"], 'password':request.POST["password"]}
            if form["username"] and form["password"]:
                user = authenticate(username=form['username'], password=form['password'])
                if user == None:
                    form['errors'] = u"Такого аккаунта нет"
                    return render(request,'authorization.html',{'form':form})
                else:
                    login(request, user)
                    return redirect('site')
            else:
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'authorization.html',{'form': form})
        else:
            return render(request, 'authorization.html', {})
    else:
        return redirect('site')



