from django.contrib import admin
from . models import Product,Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price','stock','available','created','updated']
    prepopulated_fields = {'slug':('name',)}
    list_editable = ['price','available','stock']
admin.site.register(Product,ProductAdmin)