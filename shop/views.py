from django.shortcuts import render
from django.urls import reverse
from django.views import generic as views
from django.db.models import Q, Max
from django.contrib.auth import mixins as auth_mixins

from . import models


class ProductsView(views.ListView):
    model = models.Product
    context_object_name = 'products'

    def get_context_data(self):
        context = super().get_context_data()
        context['categories'] = models.Category.objects.all()
        context['manufactors'] = models.Manufacture.objects.all()
        context['max_price'] = models.Product.objects.aggregate(Max('price'))['price__max']
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if not self.request.GET:
            return models.Product.objects.all()

        if max_price := self.request.GET['max_price']:
            queryset = queryset.filter(price__range=(0, max_price))

        if name := self.request.GET.get('name'):
            queryset = queryset.filter(name__icontains=name)

        if (categories := self.request.GET.getlist('category')) and '__all__' not in categories:
            queryset = queryset.filter(category__in=categories)

        if (manufactors := self.request.GET.getlist('manufactor')) and '__all__' not in manufactors:
            queryset = queryset.filter(manufacture__in=manufactors)

        return queryset


class ProductView(views.DetailView):
    model = models.Product
