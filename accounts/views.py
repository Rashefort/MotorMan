from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.shortcuts import redirect
from django.shortcuts import render



class RegisterView(FormView):
    form_class = UserCreationForm
    template_name = 'signup.html'

    def form_valid(self, form):
        if self.request.recaptcha_is_valid:
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)
            login(self.request, user)

            return redirect('articles')

        return render(self.request, 'signup.html', self.get_context_data())
