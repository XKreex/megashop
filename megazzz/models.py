from django.db import models
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(in_stock=Shop.Status.INSTOCK)

# Create your models here.
class Shop(models.Model):
    class Status(models.IntegerChoices):
        OUTSTOCK = 0, 'Закончились'
        INSTOCK = 1, 'В наличии'

    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    in_stock = models.BooleanField(choices=Status.choices, default=Status.OUTSTOCK)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='posts')

    objects = models.Manager()
    published = PublishedManager()


    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])
        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
