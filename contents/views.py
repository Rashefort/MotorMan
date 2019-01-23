from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.shortcuts import render
from .models import Article

from hashlib import md5



def gravatar(request, size=40):
    if request.user.is_authenticated:
        return f'{md5(request.user.email.encode()).hexdigest()}?s={size}&d=mp'
    else:
        return None


def articles(request):
    articles = Article.objects.order_by('-date')
    populars = Article.objects.order_by('-date').order_by('-views')[:5]
    lastnews = articles[:5]

    data = {
        'avatar': gravatar(request),
        'articles': articles,
        'populars': populars,
        'lastnews': lastnews,
    }

    return render(request, 'motorman_news.html', data)


def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)

    visits = request.session.get('visits', [])
    if pk not in visits:
        visits.append(pk)
        request.session['visits'] = visits
        article.views += 1
        article.save()

    # request.session['visits'] = visits + 1
    # del request.session['visits']

    print('visits = ', visits)

    # if pk not in visits:
    #     request.session['visits'] = visits.append(pk)
    #     article.views += 1
    #     article.save()

    # request.session.modified = True

    populars = Article.objects.order_by('-date').order_by('-views')[:5]
    lastnews = Article.objects.order_by('-date')[:5]

    data = {
        'avatar': gravatar(request),
        'article': article,
        'populars': populars,
        'lastnews': lastnews,
    }

    return render(request, 'motorman_detail.html', data)


def contacts(request):
    data = {
        'avatar': gravatar(request)
    }

    return render(request, 'motorman_contacts.html', data)
