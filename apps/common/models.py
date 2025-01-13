from django.db import models

# Create your models here.

class Meta:
    abstract = True

class BaseModel(models.Model):  
    created_at = models.DateTimeField(auto_now_add=True)



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
    image = models.ImageField(upload_to='2_project/',null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    poster = models.CharField(max_length=250)
    body = models.TextField()
    seller = models.ForeignKey(Seller,on_delete=models.CASCADE)


class PortfolioPrice(models.Model):
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits = 100, decimal_places = 100)
    portfolio = models.ForeignKey(Portfolio,on_delete=models.CASCADE)
    deadline = models.IntegerField()


class PortfolioPriceOption(BaseModel):
    option = models.CharField(max_length= 200)
    portfolio_price = models.ForeignKey(PortfolioPrice,on_delete=models.CASCADE)



class Like(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.PROTECT)
    
    
    
    

    #user = models.ForeignKey(User,on_delete=models.PROTECT) 
 



#  user account uchun model


class User(models.Model):
    name = models.CharField(max_length=100)
    user_banner = models.ImageField(upload_to=...)
    user_photo = models.ImageField(upload_to=...)
    user_info = models.TextField()
    location = models.CharField(max_length=200)
    # location = models.ForeignKey(Seller, on_delete=models.CASCADE)
    created_at = models.ForeignKey(BaseModel,on_delete=models.CASCADE)








