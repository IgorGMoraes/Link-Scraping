from django.contrib import admin

from .models import ParentLink, ChildLink

admin.site.site_header = "Link Scraping Admin"
admin.site.site_title = "Link Scraping Admin Area"

class ChildLinkInline(admin.TabularInline):
    model = ChildLink

class ParentLinkAdmin(admin.ModelAdmin):
    fieldsets = [('URL', {'fields': ['url']}),]
    inlines = [ChildLinkInline]

admin.site.register(ParentLink, ParentLinkAdmin)