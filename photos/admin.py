from django.contrib import admin

from .models import Category, Photo

class CategoryAdmin(admin.ModelAdmin):
    list_display= ['name']
    search_fields = ('name',)

admin.site.register(Category, CategoryAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display=['category', 'image', 'description']
    search_fields = ('category', 'description',)
    
admin.site.register(Photo, PhotoAdmin)
    
    

