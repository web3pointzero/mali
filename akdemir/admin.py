from django.contrib import admin
from mali.akdemir.models import Haber, Makale, Notdefteri
from django.db import models

class HaberAdmin(admin.ModelAdmin):
    fieldsets  = (
        (None, {'classes': ['edit'], 'fields': ('title', 'content','publication_date',)}),
    )
    
    class Media:
        js = ['/static/js/jquery-1.6.1.min.js', '/static/js/tiny_mce/tiny_mce.js', '/static/js/textareas.js']

admin.site.register(Haber, HaberAdmin)

class MakaleAdmin(admin.ModelAdmin):
    fieldsets  = (
        (None, {'classes': ['edit'], 'fields': ('title', 'content', 'author', 'publication_date',)}),
    )
    
    class Media:
        js = ['/static/js/jquery-1.6.1.min.js', '/static/js/tiny_mce/tiny_mce.js', '/static/js/textareas.js']

admin.site.register(Makale, MakaleAdmin)

class NotdefteriAdmin(admin.ModelAdmin):
    fieldsets  = (
        (None, {'classes': ['edit'], 'fields': ('title', 'content', 'author', 'publication_date',)}),
    )
    
    class Media:
        js = ['/static/js/jquery-1.6.1.min.js', '/static/js/tiny_mce/tiny_mce.js', '/static/js/textareas.js']

admin.site.register(Notdefteri, NotdefteriAdmin)

