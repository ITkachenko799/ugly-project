# Generated by Django 3.2.8 on 2021-10-31 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Smartphone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('diagonal', models.CharField(max_length=64, verbose_name='Диагональ')),
                ('display_type', models.CharField(max_length=64, verbose_name='Тип дисплея')),
                ('resolution', models.CharField(max_length=64, verbose_name='Разрешение экрана')),
                ('accum_volume', models.CharField(max_length=64, verbose_name='Объем батареи')),
                ('ram', models.CharField(max_length=64, verbose_name='Оперативная память')),
                ('sd_volume', models.CharField(max_length=64, verbose_name='Размер внутренней памяти')),
                ('main_cam', models.CharField(max_length=64, verbose_name='Камера')),
                ('frontal_cam', models.CharField(max_length=64, verbose_name='Фронтальная камера')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Notebook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='Наименование')),
                ('slug', models.SlugField(unique=True)),
                ('image', models.ImageField(upload_to='', verbose_name='Изображение')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=16)),
                ('diagonal', models.CharField(max_length=64, verbose_name='Диагональ')),
                ('display_type', models.CharField(max_length=64, verbose_name='Тип дисплея')),
                ('processor_freq', models.CharField(max_length=64, verbose_name='Частота процессора')),
                ('ram', models.CharField(max_length=64, verbose_name='Оперативная память')),
                ('video_cart', models.CharField(max_length=64, verbose_name='Видеокарта')),
                ('time_work', models.CharField(max_length=64, verbose_name='Время работы')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category', verbose_name='Категория')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]