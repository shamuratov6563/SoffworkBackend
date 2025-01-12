from django.contrib import admin
from .models import *


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'seller',)
    search_fields = ('title',)
    list_filter = ('seller',)


admin.site.register(Kwork)
admin.site.register(Category)

