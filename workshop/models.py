import datetime
import time

from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class ServiceCategory(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, default=datetime.time())

    def get_absolute_url(self):
        return reverse("workshop:service_category_detail_url", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title', 'description']
        verbose_name = 'Категория услуги'
        verbose_name_plural = 'Категории услуг'


class Service(models.Model):
    title = models.CharField(max_length=30)
    price = models.IntegerField()
    description = models.CharField(max_length=250, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, default=datetime.datetime.now())
    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='services',
        default=slug
    )

    def get_absolute_url(self):
        return reverse("services:service_detail_url", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['title', 'price', 'description']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
