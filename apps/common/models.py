from django.db import models


# #PORTFOLIO
# class TypeOfService(models.Model):
#     type_of_service = models.CharField(max_length=100)
#     uploaded_at = models.DateTimeField(auto_now_add=True)
# class Category_select(models.Model):
#     category = models.CharField(max_length=100)
#     add_type_of_services = models.ManyToManyField(TypeOfService, related_name="services")
#     uploaded_at = models.DateTimeField(auto_now_add=True)

# class OneCategory(models.Model):
#     title = models.CharField(max_length=250)
#     select_category = models.ManyToManyField(Category_select, related_name="categories")

# class Basic_information(models.Model):
#     title =models.CharField(max_length=70)
#     category=models.ForeignKey(OneCategory,on_delete=models.CASCADE)
#     kwork_cover_image=models.ImageField(upload_to="kwork_image/",null=True)

# class Attach_files(models.Model):
#     type_of_service = models.FileField(upload_to="files/")
#     uploaded_at = models.DateTimeField(auto_now_add=True)

# class Description_and_files(models.Model):
#     description = models.TextField()
#     attach_files1 = models.ManyToManyField(Attach_files, related_name="description_and_files_1")
#     order_requirements = models.TextField()
#     attach_files2 = models.ManyToManyField(Attach_files, related_name="description_and_files_2")

class Extra_options(models.Model):
    title = models.CharField(max_length=40)
    hour = [(i, '$' + str(i)) for i in range(1, 240, 3)]
    price_of_1_kwork = models.IntegerField(choices=hour, default='$1')
    days = [(i, str(i) + ' days') for i in range(0, 11)]
    delivery = models.IntegerField(choices=days, default='0 days')
    description = models.CharField(max_length=100)
    uploaded_at = models.DateTimeField(auto_now_add=True)


class Prices_and_Services(models.Model):
    scope_of_this_kwork = models.CharField(max_length=250)

    hour = [(i, '$' + str(i)) for i in range(8, 304, 8)]

    price_of_1_kwork = models.IntegerField(choices=hour, default='$8')

    days = [(i, str(i) + ' days') for i in range(1, 31)]

    delivery = models.IntegerField(choices=days, default="1 days")

    extra_options = models.ManyToManyField(Extra_options, related_name="options")


#PORTFOLIO

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
    seller = models.ForeignKey(Seller, on_delete=models.PROTECT)
    skill = models.ForeignKey(Skill, on_delete=models.PROTECT)


class Comment(BaseModel):
    #    user = models.ForeignKey(User,on_delete=models.PROTECT)
    reply_to = models.ForeignKey("self", on_delete=models.CASCADE)
    body = models.TextField()


#Buyer

class Category(BaseModel):
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='2_project/', null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE)


class Kwork(models.Model):
    title = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='kwork_image/')
    description = models.TextField()
    order_requirements = models.TextField()


class Frequently_Asked_Questions(models.Model):
    question = models.CharField(max_length=80)
    answer = models.TextField()


class Portfolio(models.Model):
    title = models.CharField(max_length=200)
    poster = models.CharField(max_length=250)
    body = models.TextField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)


class PortfolioPrice(models.Model):
    type = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=100, decimal_places=100)
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    deadline = models.IntegerField()


class PortfolioPriceOption(BaseModel):
    option = models.CharField(max_length=200)
    portfolio_price = models.ForeignKey(PortfolioPrice, on_delete=models.CASCADE)


class Like(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.PROTECT)
