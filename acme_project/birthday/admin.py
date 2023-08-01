from django.contrib import admin

from .models import Tag

class TagAdmin(admin.ModelAdmin):
    list_display = ('tag')


admin.site.register(Tag)
