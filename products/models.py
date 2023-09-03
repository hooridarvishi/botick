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
    phone=models.CharField(max_length=20, verbose_name="شماره موبایل" ,  default="")
    email=models.EmailField(max_length=20, verbose_name="ایمیل" , default="")
    # objects = models.Manager()
    objects = jmodels.jManager()
    published = PublishedManager()
    old_price=models.CharField(max_length=12,default="")
    discount=models.CharField(max_length=12 , default="")    
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
    created = jmodels.jDateTimeField(auto_now_add=True)
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


#
# class ContactModel(models.Model):
#     message = models.TextField(verbose_name="پیام")
#     name = models.CharField(max_length=250, verbose_name="نام")
#     email = models.EmailField(verbose_name="ایمیل")
#     phone = models.CharField(max_length=11, verbose_name="شماره تماس")
#     subject = models.CharField(max_length=250, verbose_name="موضوع")
#     class Meta:
#         verbose_name = "راه ارتباطی"
#         verbose_name_plural="راه های ارتباطی"
#     def __str__(self):
#         return self.subject


class ContactModel(models.Model):

    body = models.CharField(max_length=120, verbose_name="پیام")
    name = models.CharField(max_length=250, verbose_name="نام")
    email = models.EmailField(verbose_name="ایمیل")
    active = models.BooleanField(default=False, verbose_name="وضعیت")

    # class Meta:
    #     ordering = ["name"],
    #     indexes = [models.Index(fields=["name"])]
    #
    # def __str__(self):
    #     return self.name
    #

class CommentModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, related_name="comments")
    title= models.CharField(max_length=250, verbose_name="عنوان نظر", default="")
    # name = models.CharField(max_length=250, verbose_name="نام", default="")
    message_positive_points = models.TextField(max_length=250, verbose_name=" نکات مثبت", default="")
    message_negative_points=models.TextField(max_length=250, verbose_name=" نکات منفی", default="")
    message_text=models.TextField(max_length=250, verbose_name=" متن پیام ", default="")
    created = jmodels.jDateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")
    updated = models.DateTimeField(auto_now=True, verbose_name="تاریخ ویرایش")
    active = models.BooleanField(default=False, verbose_name="وضعیت")
    email = models.EmailField(max_length=250, verbose_name="ایمیل", default="")
    # body = models.TextField(max_length=250,verbose_name="متن کامنت" ,default="text")
    phone = models.TextField(max_length=250, verbose_name=" تلفن", default="")

    class Meta:
        ordering = ["created"]
        indexes = [models.Index(fields=["created"])]
        verbose_name = "کامنت"
        verbose_name_plural = "کامنت ها"

    def __str__(self):
        return f"{self.name}: {self.product}"

class Account(models.Model):

    user=models.OneToOneField(User,related_name="account",verbose_name="",on_delete=models.CASCADE)
    date_of_birth=jmodels.jDateField(verbose_name="تاریخ تولد " , blank=True , null=True)
    bio=models.TextField(verbose_name=" بیوگرافی " , blank=True , null=True)
    photo=ResizedImageField(upload_to="profile_image/",size=[500 , 500] ,crop=["middle","center"] , quality=60,blank=True , null=True )
    job=models.CharField(max_length=120,verbose_name=" شغل " , blank=True , null=True)
    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name="اکانت"
        verbose_name_plural="اکانت ها "