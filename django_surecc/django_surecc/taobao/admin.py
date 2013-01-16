from django.contrib import admin 
from django_surecc.taobao.models import Category, Seller, Commidity, Picture

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'coding')
    search_fields = ('name', 'coding')
    
class SellerAdmin(admin.ModelAdmin):
    list_display = ('name', 'domain')
    search_fields = ('name', 'domain')
    
class PictureAdmin(admin.ModelAdmin):
    list_display = ('dir', 'var_total', 'commidity')
    
class CommidityAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'url')
    search_fields = ('name', 'category', 'seller')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Seller, SellerAdmin)
admin.site.register(Commidity, CommidityAdmin)
admin.site.register(Picture, PictureAdmin)