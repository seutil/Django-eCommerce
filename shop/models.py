from django.db import models


class Category(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', null=True, blank=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Manufacture(models.Model):
    name = models.CharField('Имя', max_length=100)
    description = models.TextField('Описание', null=True, blank=True)
    url = models.URLField('Сайт', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'


class Product(models.Model):
    name = models.CharField('Название', max_length=100)
    description = models.TextField('Описание', null=True, blank=True)
    price = models.PositiveIntegerField('Стоимость', help_text='Указывать стоимость в рублях')
    category = models.ForeignKey(Category, models.DO_NOTHING, related_name='products', verbose_name='Категория')
    manufacture = models.ForeignKey(Manufacture, models.DO_NOTHING, related_name='products', verbose_name='Производитель')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductImage(models.Model):
    title = models.CharField('Заголовок', max_length=100, null=True, blank=True)
    image = models.ImageField('Изображение', upload_to='product/')
    product = models.ForeignKey(Product, models.CASCADE, related_name='images', verbose_name='Продукт')

    class Meta:
        verbose_name = 'Фотография продукта'
        verbose_name_plural = 'Фотографии продуктов'
