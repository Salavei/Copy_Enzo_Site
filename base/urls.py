from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('find/', views.find, name='find'),
    path('broadcast/', views.broadcast, name='broadcast'),

    path('vino/', views.VinoListView.as_view(), name='vino'),
    path('vacancies/', views.VacanciesCreateView.as_view(), name='vacancies'),
    path('photos', views.PhotosListView.as_view(), name='photos'),
    path('news/', views.NewsListView.as_view(), name='news'),
    path('menu/main-menu/', views.menu, name='menu'),
    path('menu/lunch-menu-of-the-week/', views.lunch_menu, name='lunch_menu'),

]
