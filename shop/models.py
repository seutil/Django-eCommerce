from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Manufacture(models.Model):
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание')
    url = models.URLField('Сайт')


class Product(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', null=True, blank=True)
    price = models.PositiveIntegerField('Стоимость', help_text='Указывать стомиость в рублях')
    category = models.ForeignKey(Category, models.DO_NOTHING, related_name='products')
    manufacture = models.ForeignKey(Manufacture, models.DO_NOTHING, related_name='products')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    title = models.CharField('Заголовок', max_length=100, null=True, blank=True)
    image = models.ImageField('Изобржение')
    product = models.ForeignKey(Product, models.CASCADE, related_name='images')
