from django.contrib import admin
from sports.models import Category, Product
# Register your models here.


admin.site.register([Category])


@admin.register(Product)
class SportAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'picture')
