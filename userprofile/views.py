from django.shortcuts import redirect
from django.shortcuts import render
from django.db import transaction

from userprofile.forms import UserForm
from userprofile.forms import ProfileForm
from contents.views import gravatar


@transaction.atomic
def profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

            return redirect('articles')

    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    data = {
        'avatar': gravatar(request),
        'user_form': user_form,
        'profile_form': profile_form
    }

    return render(request, 'userprofile.html', data)
