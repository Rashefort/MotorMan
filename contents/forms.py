from django import forms



class ProfileForm(forms.Form):
    EXPERIENCE = [('1', 'Начинающий'), ('2', 'Любитель'), ('3', 'Профессионал')]
    SEX = [('1', 'Не сообщаю'), ('2', 'Мужчина'), ('3', 'Женщина')]

    email = forms.EmailField(label='Email address', max_length=254, required=False)
    place = forms.CharField(label='Место жительства', max_length=30, required=False)
    experience = forms.ChoiceField(label='Опыт вождения', choices=EXPERIENCE)
    sex = forms.ChoiceField(label='Пол', choices=SEX)
