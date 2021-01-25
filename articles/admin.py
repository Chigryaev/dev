from django.contrib import admin
from .models import Article, Category

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Article, AuthorAdmin)
admin.site.register(Category, AuthorAdmin)
