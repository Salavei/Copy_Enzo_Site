from django.db import models
from .service import vacancy_alert


class News(models.Model):
    title = models.CharField(max_length=200, verbose_name='Описание')
    body = models.TextField(verbose_name='Текст новости')
    photo = models.ImageField(verbose_name='Фотография')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'Новости'
        verbose_name_plural = 'Новость'


class Photo(models.Model):
    name = models.CharField(unique=True, max_length=200, verbose_name='Описание фото')
    photo = models.ImageField(verbose_name='Фотография')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Фотографии'
        verbose_name_plural = 'Фотография'


class Vine(models.Model):
    title = models.CharField(max_length=200, verbose_name='Описание Новости о Вине')
    body = models.TextField(verbose_name='Текст Новости о Вине')
    photo = models.ImageField(verbose_name='Фотография для Новости о Вине')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']
        verbose_name = 'О Винах'
        verbose_name_plural = 'О Вине'


class Vacancy(models.Model):
    CHOICE_VACANCY = [
        ('Официант', 'Официант'),
        ('Повар горячего цеха', 'Повар горячего цеха'),
        ('Повар холодного цеха', 'Повар холодного цеха'),
    ]
    type_vacancy = models.CharField(max_length=51, choices=CHOICE_VACANCY)
    name_lastname = models.CharField(max_length=200, verbose_name='ФИО')
    phone_number = models.CharField(max_length=51, verbose_name='Номер телефона')
    email = models.CharField(max_length=30, verbose_name='Email')
    date_birthday = models.CharField(max_length=51, verbose_name='Дата рождения')
    education = models.TextField(verbose_name='Образование')
    work_experience = models.TextField(verbose_name='Опыт работы')
    recommendations = models.TextField(verbose_name='Рекомендации')
    # изменить потом на сохранение файлов
    resume = models.ImageField(verbose_name='Резюме')

    def __str__(self):
        return "{}, {}".format(self.name_lastname, self.type_vacancy)

    def save(self, *args, **kwargs):
        super(Vacancy, self).save(*args, **kwargs)
        vacancy_alert(self.email, self.name_lastname)

    class Meta:
        verbose_name = 'Резюме'
        verbose_name_plural = 'Резюме'


class Menu(models.Model):
    DATE_MENU = [
        ('main_menu', 'основное меню'),
        ('lunch_menu', 'обеденное меню недели'),
    ]
    TYPE_MENU = [

        ('Appetizers_salads', 'Закуски и салаты'),
        ('Breakfasts', 'Завтраки'),
        ('Bread', 'Хлеб'),
        ('Dessert', 'Десерт'),
        ('Drinks', 'Напитки'),
        ('Hot_meals', 'Горячие блюда'),
        ('Snacks', 'Закуски'),
        ('Salads', 'Салаты'),
        ('Burgers', 'Бургеры'),
        ('Steaks', 'Стейки'),
        ('Fish', 'Рыба'),
        ('Soups', 'Супы'),
        ('Garnishes', 'Гарниры'),
        ('Sauces', 'Соусы'),
        ('Desserts', 'Десерты'),
        ('Freshies', 'Фреши'),
        ('Drinks', 'Напитки'),
        ('Coffee', 'Кофе (Honduras San Marcos, Kitchen Coffee Roasters)'),
    ]
    type_date_menu = models.CharField(choices=DATE_MENU, max_length=51, verbose_name='Типы Меню')
    type_menu = models.CharField(choices=TYPE_MENU, max_length=51, verbose_name='Виды Блюда')
    name = models.CharField(max_length=51, verbose_name='Название Блюда')
    grams = models.IntegerField(verbose_name='Граммовки Блюда')
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='Стоимость Блюда')

    def __str__(self):
        return "{}, {}".format(self.type_date_menu, self.name)

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
