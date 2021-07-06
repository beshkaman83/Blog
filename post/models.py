from django.db import models
from django.conf import settings


class Tag(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='Слаг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Category(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    slug = models.SlugField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, verbose_name='Автор')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    tags = models.ManyToManyField(Tag, verbose_name='Теги')
    slug = models.SlugField(verbose_name='Слаг')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
