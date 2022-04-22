from django import forms
from .models import Vacancy


class VacancyForm(forms.ModelForm):
    CHOICE_VACANCY = [
        ('Официант', 'Официант'),
        ('Повар горячего цеха', 'Повар горячего цеха'),
        ('Повар холодного цеха', 'Повар холодного цеха'),
    ]
    type_vacancy = forms.ChoiceField(choices=CHOICE_VACANCY, widget=forms.Select(attrs={
        'placeholder': 'ВЫБОР ВАКАНСИИ',
        'class': 'jq-selectbox'
    }))
    name_lastname = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'ФИО',
        'class': 'required'
    }))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Телефон',
        'class': 'required'
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'placeholder': 'E-mail',
        'class': 'required'
    }))
    date_birthday = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Дата рождения',
        'class': 'required'
    }))
    education = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Образования',
        'class': 'required'
    }))
    work_experience = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Ваш опыт работы и достижения',
        'class': 'required'
    }))
    recommendations = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Рекомендации',
        'class': 'required'
    }))
    resume = forms.ImageField(widget=forms.FileInput(attrs={
        'placeholder': 'Прикрепить фото/резюме',
        'class': 'btn-file'
    }))

    class Meta:
        model = Vacancy
        fields = '__all__'

