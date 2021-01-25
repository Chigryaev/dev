from django.contrib import admin


from .models import Action, Tracking


# Register your models here.
class ActionAdmin(admin.ModelAdmin):
    list_display = ("user", "verb", "target", "datetime")
    list_filter = ("datetime",)
    search_fields = ("verb",)


admin.site.register(Action, ActionAdmin)
admin.site.register(Tracking)