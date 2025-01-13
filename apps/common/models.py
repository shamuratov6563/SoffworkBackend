from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from apps.users.models import User, BaseModel
from django_ckeditor_5.fields import CKEditor5Field


class Skill(BaseModel):
    name = models.CharField(max_length=250)
class Seller(BaseModel):
 #   user = models.ForeignKey(User, on_delete=models.PROTECT)
    country = models.CharField(max_length=250)
    about = models.TextField()

    
class SellerSkill(models.Model):
    seller = models.ForeignKey(Seller,on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill,on_delete=models.PROTECT)


class Comment(BaseModel):
#    user = models.ForeignKey(User,on_delete=models.PROTECT)
    reply_to = models.ForeignKey("self", on_delete=models.CASCADE)
    body = models.TextField()


#Buyer

class Category(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='categories/', null=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    order = models.IntegerField(default=1)


class ServiceType(BaseModel):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Kwork(models.Model):
    class KworkStatus(models.TextChoices):
        ACTIVE = 'active', _('Active')
        MODERATION = 'moderation', _('Moderation')
        CANCELED = 'canceled', _('Canceled')
        DELETED = 'deleted', _('Deleted')
    title = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='kwork_posters/')
    description = CKEditor5Field('Description', config_name='extends')
    order_requirements = CKEditor5Field('Order requirements', config_name='extends')
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50, choices=KworkStatus.choices, default=KworkStatus.MODERATION)


class KworkFeedback(BaseModel):
    kwork = models.ForeignKey(Kwork, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()


class KworkServiceType(BaseModel):
    kwork = models.ForeignKey(Kwork, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)


class KworkFile(BaseModel):
    kwork = models.ForeignKey(Kwork, on_delete=models.CASCADE)
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
    seller = models.ForeignKey(User, on_delete=models.CASCADE)


class PortfolioFile(BaseModel):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    file = models.FileField(upload_to='portfolio_files/')
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)



class Like(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.PROTECT)
    
    
    
    

    #user = models.ForeignKey(User,on_delete=models.PROTECT) 




#  user account uchun model


class User(BaseModel):
    name = models.CharField(max_length=100)
    user_banner = models.ImageField(upload_to=...)
    user_photo = models.ImageField(upload_to=...)
    user_info = models.TextField()
    location = models.CharField(max_length=200)
    # location = models.ForeignKey(Seller, on_delete=models.CASCADE)








