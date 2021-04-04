from django.contrib import admin
from .models import Comment

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Comment, AuthorAdmin)
