from django.contrib import admin
from .models import *


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    search_fields = ('name',)


admin.site.register(Kwork)

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'parent', 'order')
    list_filter = ('parent',)
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}


