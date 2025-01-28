from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'parent', 'order')
    list_filter = ('parent',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Kwork)
class KworkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'seller', 'status', 'created_at')
    list_filter = ('status', 'category', 'seller')
    search_fields = ('title', 'description')
    list_editable = ('status',)

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'seller', 'cover_image')
    list_filter = ('category', 'seller')
    search_fields = ('title', 'description')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'commentator', 'body', 'kwork', 'created_at')
    list_filter = ('commentator', 'kwork')
    search_fields = ('body',)

@admin.register(SellerSkill)
class SellerSkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'seller', 'skill')
    search_fields = ('seller__username', 'skill__name')

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category')
    list_filter = ('category',)
    search_fields = ('title',)

@admin.register(KworkFeedback)
class KworkFeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'kwork', 'admin', 'text', 'created_at')
    search_fields = ('text',)

@admin.register(KworkFile)
class KworkFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'kwork', 'file')
    search_fields = ('file',)

@admin.register(PortfolioFile)
class PortfolioFileAdmin(admin.ModelAdmin):
    list_display = ('id', 'portfolio', 'file', 'service_type')
    search_fields = ('file',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'portfolio', 'user')
    search_fields = ('user__username', 'portfolio__title')

@admin.register(KworkExtraOption)
class KworkExtraOptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'scopes', 'price_of_kwork', 'delivery_time')
    search_fields = ('scopes',)
