from django.db import models
from datetime import date
from django.shortcuts import reverse




class Category(models.Model):
    name=models.CharField(max_length=150,verbose_name='Категория')
    description=models.TextField(verbose_name='Описание')
    url=models.SlugField(max_length=160,unique=True,verbose_name='Слаг')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'


class Actor(models.Model):
    name=models.CharField(max_length=100,verbose_name='Имя')
    age=models.DateField(default=date.today,verbose_name='Возраст')
    description=models.TextField(verbose_name='Описание')
    image=models.ImageField(upload_to='actors/',verbose_name='Изображение')


    def get_absolute_url(self):
        return reverse('actor_detail',kwargs={'id':self.id})


    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Актеры и режисеры'
        verbose_name_plural='Актеры и режисеры'



class Genre(models.Model):
    name=models.CharField(max_length=100,verbose_name='Имя')
    description=models.TextField(verbose_name='Описание')
    url=models.SlugField(max_length=100,unique=True,verbose_name='Слаг')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name='Жанр'
        verbose_name_plural='Жанры'


class Movie(models.Model):
    title=models.CharField(max_length=100,verbose_name='Название')
    tagline=models.CharField(max_length=100,default=' ',verbose_name='Слоган')
    description=models.TextField(verbose_name='Описание')
    poster=models.ImageField(upload_to='movies/',verbose_name='Постер')
    year=models.PositiveSmallIntegerField(default=2019,verbose_name='Дата выхода')
    country=models.CharField(max_length=30,verbose_name='Страна')
    directors=models.ManyToManyField(Actor,verbose_name='Режисер',related_name='film_director')
    actors=models.ManyToManyField(Actor,verbose_name='Актеры',related_name='film_actor')
    genres=models.ManyToManyField(Genre,verbose_name='Жанры',related_name='film_genres')
    world_premiere=models.DateField(default=date.today,verbose_name='Примьера в мире')
    budget=models.PositiveIntegerField(default=0,help_text='указывать сумму в долларах',verbose_name='Бюджет')
    fees_in_usa= models.PositiveIntegerField( default=0, help_text='указывать сумму в долларах',verbose_name='Сборы в США')
    fees_in_world = models.PositiveIntegerField( default=0, help_text='указывать сумму в долларах',verbose_name='Сборы в мире')
    category=models.ForeignKey(Category,verbose_name='Категория',on_delete=models.SET_NULL,null=True)
    url=models.SlugField(max_length=130,unique=True,verbose_name='Слаг')
    draft=models.BooleanField(default=False,verbose_name='Черновик')



    def get_absolute_url(self):
        return reverse('movie',kwargs={'slug':self.url})


    def __str__(self):
        return self.title



    class Meta:
        verbose_name='Фильм'
        verbose_name_plural='Фильмы'


class MovieShots(models.Model):
    title=models.CharField(max_length=100,verbose_name='Заголовок')
    description=models.TextField(verbose_name='Описание')
    image=models.ImageField(upload_to='movie_shots/',verbose_name='Фото')
    movie=models.ForeignKey(Movie,related_name='movieshots',verbose_name='Фильм',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='Кадр из фильма'
        verbose_name_plural='Кадры из фильма'


class RatingStar(models.Model):
    value=models.PositiveSmallIntegerField(default=0,verbose_name='Значение')

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name='Звезда рейтинга'
        verbose_name_plural='Звезды рейтинга'
        ordering=['-value']

class Rating(models.Model):
    ip=models.CharField(max_length=15,verbose_name='IP адрес')
    star=models.ForeignKey(RatingStar,on_delete=models.CASCADE,verbose_name='звезда')
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE,verbose_name='фильм',related_name='ratings')

    def str(self):
        return f'{self.star} - {self.movie}'

    class Meta:
        verbose_name='Рейтинг'
        verbose_name_plural='Рейтинги'


class Review(models.Model):
    email=models.EmailField(verbose_name='Email')
    name=models.CharField(max_length=100,verbose_name='Имя')
    text=models.TextField(max_length=5000,verbose_name='Ваш комментарий')
    parent=models.ForeignKey('self',verbose_name='Родитель',on_delete=models.SET_NULL,blank=True,null=True,related_name='children')
    movie=models.ForeignKey(Movie,verbose_name='Фильм',on_delete=models.CASCADE,related_name='reviews')

    def __str__(self):
        return f'{self.name} - {self.movie}'

    class Meta:
        verbose_name='Отзыв'
        verbose_name_plural='Отзывы'



