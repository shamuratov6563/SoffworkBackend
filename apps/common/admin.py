# from django.contrib import admin
# from .models import *

# # Register your models here.

# @admin.register(Skill)
# class SkillAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'created_at')
#     search_fields = ('name',)

# @admin.register(Seller)
# class SellerAdmin(admin.ModelAdmin):
#     list_display = ('id', 'country', 'created_at')
#     search_fields = ('country',)

# @admin.register(SellerSkill)
# class SellerSkillAdmin(admin.ModelAdmin):
#     list_display = ('id', 'seller', 'skill')
#     list_filter = ('seller',)

# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'reply_to', 'body', 'created_at')
#     search_fields = ('body',)

# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'parent', 'created_at')
#     search_fields = ('title',)

# @admin.register(Portfolio)
# class PortfolioAdmin(admin.ModelAdmin):
#     list_display = ('id', 'title', 'seller',)
#     search_fields = ('title',)
#     list_filter = ('seller',)

# @admin.register(PortfolioPrice)
# class PortfolioPriceAdmin(admin.ModelAdmin):
#     list_display = ('id', 'portfolio', 'type', 'price', 'deadline')
#     list_filter = ('portfolio',)

# @admin.register(PortfolioPriceOption)
# class PortfolioPriceOptionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'option', 'portfolio_price')
#     list_filter = ('portfolio_price',)

# @admin.register(Like)
# class LikeAdmin(admin.ModelAdmin):
#     list_display = ('id', 'portfolio')
#     list_filter = ('portfolio',)

