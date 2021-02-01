from django.contrib import admin
# Register your models here.
from product.models import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','cpu','ram','gpu','battery','volume','weight','display','maker','sw_os','price','image','content') # 사이트에서 출력할 컬럼 목록
