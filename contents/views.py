from django.shortcuts import redirect
from django.shortcuts import render

from .forms import ProfileForm
from .models import Article

from hashlib import md5



def gravatar(request, size=40):
    if request.user.is_authenticated:
        return f'{md5(request.user.email.encode()).hexdigest()}?s={size}&d=mp'
    else:
        return None


def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            request.user.email = form.cleaned_data.get('email')
            request.user.first_name = form.cleaned_data.get('place')

            experience = form.cleaned_data.get('experience')
            sex = form.cleaned_data.get('sex')
            request.user.last_name = f'{experience} {sex}'

            request.user.save()

            return redirect('articles')

    else:
        try:
            email = request.user.email
            place = request.user.first_name
            experience, sex = request.user.last_name.split()

        except ValueError:
            sex = experience = '1'

        finally:
            data = {'email': email, 'place': place, 'sex': sex, 'experience': experience}

        form = ProfileForm(initial=data)

    return render(request, 'motorman_profile.html', {'avatar': gravatar(request), 'form': form})


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


def contacts(request):
    data = {
        'avatar': gravatar(request)
    }

    return render(request, 'motorman_contacts.html', data)
