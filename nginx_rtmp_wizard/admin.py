from django.contrib import admin

from . import models


@admin.register(models.Server)
class ServerAdmin(admin.ModelAdmin):
    pass


class PushInline(admin.TabularInline):
    model = models.Push


@admin.register(models.Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'name', 'live']
    list_display_links = ['__str__']
    list_editable = ['live']

    inlines = [PushInline]

