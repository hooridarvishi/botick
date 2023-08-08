from django.db import models
from django_resized import ResizedImageField
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=ProductModel.Status.PUBLISHED)


class ProductModel(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
        REJECTED = 'RJ', 'Rejected'

    # relations
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_posts", verbose_name="نویسنده")
    # data fields
    title = models.CharField(max_length=250, verbose_name="عنوان")
    description = models.TextField(verbose_name="توضیحات")
    slug = models.SlugField(max_length=250, verbose_name="اسلاگ")
    price = models.CharField(max_length=20, verbose_name="قیمت")
    publish = jmodels.jDateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")
    created = jmodels.jDateTimeField(auto_now_add=True)
    updated = jmodels.jDateTimeField(auto_now=True)
    # choice fields
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT, verbose_name="وضعیت")
    reading_time = models.PositiveIntegerField(verbose_name="زمان مطالعه")

    # objects = models.Manager()
    objects = jmodels.jManager()
    published = PublishedManager()

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]
        verbose_name = "محصول"
        verbose_name_plural = "محصول ها"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:detail', args=[self.id])


class ImageModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="images")
    image_file = ResizedImageField(upload_to="post_images/", size=[500, 500], quality=75, crop=["middle", "center"])
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=30, verbose_name="عنوان", null=True, blank=True)
    description = models.TextField(max_length=200, verbose_name="توضیحات", null=True, blank=True)

    class Meta:
        ordering = ['-title']
        indexes = [
            models.Index(fields=['-title'])
        ]
        verbose_name = "عکس"
        verbose_name_plural = "عکس ها"

    def __str__(self):
        return self.title
