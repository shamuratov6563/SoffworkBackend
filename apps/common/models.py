from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from apps.users.models import User, BaseModel
from django_ckeditor_5.fields import CKEditor5Field



class Skill(BaseModel):
    name = models.CharField(max_length=250)

    
class SellerSkill(BaseModel):
    seller = models.ForeignKey(User, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)


class Comment(BaseModel):
    commentator = models.ForeignKey(User, on_delete=models.PROTECT, related_name='commentator')
    reply_to = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    body = models.TextField()
    kwork = models.ForeignKey('Kwork', on_delete=models.CASCADE, null=True, blank=True)


class Category(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='categories/', null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='children'
    )
    order = models.IntegerField(default=1)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs): 
        if not self.slug: 
            self.slug = slugify(self.title) 
            super().save(*args, **kwargs) 
            
    def __str__(self): return self.title


class ServiceType(BaseModel):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='service_types')


class Kwork(BaseModel):
    class KworkStatus(models.TextChoices):
        ACTIVE = 'active', _('Active')
        MODERATION = 'moderation', _('Moderation')
        CANCELED = 'canceled', _('Canceled')
        DELETED = 'deleted', _('Deleted')
    title = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='kworks')
    cover_image = models.ImageField(upload_to='kwork_posters/')
    description = CKEditor5Field('Description', config_name='extends')
    order_requirements = CKEditor5Field('Order requirements', config_name='extends')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kworks')
    status = models.CharField(max_length=50, choices=KworkStatus.choices, default=KworkStatus.MODERATION)


class KworkFeedback(BaseModel):
    kwork = models.ForeignKey(Kwork, on_delete=models.CASCADE, related_name='feedbacks')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='feedbacks')
    text = models.TextField(null=True)


class KworkServiceType(BaseModel):
    kwork = models.ForeignKey(Kwork, on_delete=models.CASCADE, related_name='service_types')
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='kworks')


class KworkFile(BaseModel):
    kwork = models.ForeignKey(Kwork, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='kwork_files/')


class KworkExtraOption(BaseModel):
    scopes = models.TextField(verbose_name="Scopes")
    price_of_kwork = models.DecimalField(max_digits=100, decimal_places=100)
    delivery_time = models.IntegerField()
    description = models.TextField(null=True)


class Portfolio(BaseModel):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='portfolios')
    cover_image = models.ImageField(upload_to='cover_images/')
    seller = models.ForeignKey(User, on_delete=models.CASCADE, related_name='portfolios')


class PortfolioFile(BaseModel):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, related_name='files')
    file = models.FileField(upload_to='portfolio_files/')
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE, related_name='portfolio_files')


class Like(BaseModel):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.PROTECT, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='likes')







