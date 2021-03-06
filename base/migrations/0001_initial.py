# Generated by Django 4.0.4 on 2022-04-21 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_date_menu', models.CharField(choices=[('основное меню', 'основное меню'), ('обеденное меню недели', 'обеденное меню недели')], max_length=51, verbose_name='Типы Меню')),
                ('type_menu', models.CharField(choices=[('Закуски и салаты', 'Закуски и салаты'), ('Завтраки (подаются весь день)', 'Завтраки (подаются весь день)'), ('Горячие блюда', 'Горячие блюда'), ('Хлеб', 'Хлеб'), ('Десерт', 'Десерт'), ('Напитки', 'Напитки'), ('Горячие блюда', 'Горячие блюда'), ('Закуски', 'Закуски'), ('Салаты', 'Салаты'), ('Бургеры', 'Бургеры'), ('Стейки', 'Стейки'), ('Рыба', 'Рыба'), ('Супы', 'Супы'), ('Гарниры', 'Гарниры'), ('Соусы', 'Соусы'), ('Десерты', 'Десерты'), ('Фреши', 'Фреши'), ('Напитки', 'Напитки'), ('Кофе (Honduras San Marcos, Kitchen Coffee Roasters)', 'Кофе (Honduras San Marcos, Kitchen Coffee Roasters)')], max_length=51, verbose_name='Виды Блюда')),
                ('name', models.CharField(max_length=51, verbose_name='Название Блюда')),
                ('grams', models.IntegerField(verbose_name='Граммовки Блюда')),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Стоимость Блюда')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Описание')),
                ('body', models.TextField(verbose_name='Текст новости')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотография')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Новости',
                'verbose_name_plural': 'Новость',
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Описание фото')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотография')),
            ],
            options={
                'verbose_name': 'Фотографии',
                'verbose_name_plural': 'Фотография',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_vacancy', models.CharField(choices=[('Официант', 'Официант'), ('Повар горячего цеха', 'Повар горячего цеха'), ('Повар холодного цеха', 'Повар холодного цеха')], max_length=51)),
                ('name_lastname', models.CharField(max_length=200, verbose_name='ФИО')),
                ('phone_number', models.CharField(max_length=51, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=30, verbose_name='Email')),
                ('date_birthday', models.CharField(max_length=51, verbose_name='Дата рождения')),
                ('education', models.TextField(verbose_name='Образование')),
                ('work_experience', models.TextField(verbose_name='Опыт работы')),
                ('recommendations', models.TextField(verbose_name='Рекомендации')),
                ('resume', models.ImageField(upload_to='', verbose_name='Резюме')),
            ],
        ),
        migrations.CreateModel(
            name='Vine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Описание Новости о Вине')),
                ('body', models.TextField(verbose_name='Текст Новости о Вине')),
                ('photo', models.ImageField(upload_to='', verbose_name='Фотография для Новости о Вине')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'О Винах',
                'verbose_name_plural': 'О Вине',
            },
        ),
    ]
