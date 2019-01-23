from django.contrib.auth.models import User
from django import forms

from userprofile.models import Profile



class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('birthday', 'place', 'sex', 'experience', 'about')

# class ProfileForm(forms.Form):
#     firstname = forms.CharField(label='Имя', max_length=30, required=False)
#     lastname = forms.CharField(label='Фамилия', max_length=30, required=False)
#     email = forms.EmailField(label='Email address', max_length=254, required=False)
#     birthday = form.DateField(label='День рождения', required=False)
#     place = forms.CharField(label='Место жительства', max_length=30, required=False)

#     SEX = (
#         ('n', 'Не сообщаю'),
#         ('m', 'Мужчина'),
#         ('f', 'Женщина')
#     )

#     sex = forms.ChoiceField(label='Пол', choices=SEX)

#     EXPERIENCE = (
#         ('e', 'Начинающий'),
#         ('m', 'Любитель'),
#         ('h', 'Профессионал')
#     )

#     experience = forms.ChoiceField(label='Опыт вождения', choices=EXPERIENCE)

#     about = forms.TextField(label='О себе', max_length='700', required=False)
