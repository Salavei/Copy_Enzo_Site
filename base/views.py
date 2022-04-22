from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import News, Photo, Vine, Vacancy, Menu
from .forms import VacancyForm


def home(request):
    context = {}
    return render(request, 'base/home.html', context)


class VinoListView(ListView):
    paginate_by = 5
    model = Vine
    template_name = 'base/vino.html'


class PhotosListView(ListView):
    model = Photo
    template_name = 'base/photos.html'


class NewsListView(ListView):
    paginate_by = 5
    model = News
    template_name = 'base/news.html'


# class MenuListView(ListView):
#     model = Menu
#     template_name = 'base/menu.html'
#     def get_queryset(self):
#         return super().get_queryset().filter(type_date_menu='основное меню')


def menu(request):
    breakfasts = Menu.objects.filter(type_date_menu='main_menu', type_menu='Breakfasts')
    snacks = Menu.objects.filter(type_date_menu='main_menu', type_menu='Snacks')
    salads = Menu.objects.filter(type_date_menu='main_menu', type_menu='Salads')
    burgers = Menu.objects.filter(type_date_menu='main_menu', type_menu='Burgers')
    steaks = Menu.objects.filter(type_date_menu='main_menu', type_menu='Steaks')
    fish = Menu.objects.filter(type_date_menu='main_menu', type_menu='Fish')
    soups = Menu.objects.filter(type_date_menu='main_menu', type_menu='Soups')
    garnishes = Menu.objects.filter(type_date_menu='main_menu', type_menu='Garnishes')
    sauces = Menu.objects.filter(type_date_menu='main_menu', type_menu='Sauces')
    desserts = Menu.objects.filter(type_date_menu='main_menu', type_menu='Dessert')
    freshies = Menu.objects.filter(type_date_menu='main_menu', type_menu='Freshies')
    drinks = Menu.objects.filter(type_date_menu='main_menu', type_menu='Drinks')
    coffee = Menu.objects.filter(type_date_menu='main_menu', type_menu='Coffee')
    context = {
        'breakfasts': breakfasts,
        'snacks': snacks,
        'salads': salads,
        'burgers': burgers,
        'steaks': steaks,
        'fish': fish,
        'soups': soups,
        'garnishes': garnishes,
        'sauces': sauces,
        'desserts': desserts,
        'freshies': freshies,
        'drinks': drinks,
        'coffee': coffee,
    }
    return render(request, 'base/menu.html', context)


def lunch_menu(request):
    appetizers_salads = Menu.objects.filter(type_date_menu='lunch_menu', type_menu='Appetizers_salads')
    hot_meals = Menu.objects.filter(type_date_menu='lunch_menu', type_menu='Hot_meals')
    bread = Menu.objects.filter(type_date_menu='lunch_menu', type_menu='Bread')
    dessert = Menu.objects.filter(type_date_menu='lunch_menu', type_menu='Dessert')
    drinks = Menu.objects.filter(type_date_menu='lunch_menu', type_menu='Drinks')
    context = {
        'appetizers_salads': appetizers_salads,
        'hot_meals': hot_meals,
        'bread': bread,
        'dessert': dessert,
        'drinks': drinks,
    }
    return render(request, 'base/menu.html', context)


# class LunchMenuListView(ListView):
#     model = Menu
#     template_name = 'base/menu.html'
#     def get_queryset(self):
#         return super().get_queryset().filter(type_date_menu='обеденное меню недели')


class VacanciesCreateView(CreateView):
    model = Vacancy
    form_class = VacancyForm
    success_url = '/'
    template_name = 'base/vacancies.html'


def find(request):
    context = {}
    return render(request, 'base/find.html', context)


def broadcast(request):
    context = {}
    return render(request, 'base/broadcast.html', context)
