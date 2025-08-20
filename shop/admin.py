from django.contrib import admin
from .models import Product, Category, ProductImage, ProductVariant, CustomerProfile, Address, Order, OrderItem

# Inline for adding product variants (e.g., 100g, 250g) inside product admin
class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    extra = 1

# Product admin to include variant inline editor
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductVariantInline]


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    list_display = ("order_number", "user", "status", "payment_status", "total_price", "created_at")
    list_filter = ("status", "payment_status", "created_at")
    search_fields = ("order_number", "user__username", "user__email")
    inlines = [OrderItemInline]

# Register models
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)
admin.site.register(CustomerProfile)
admin.site.register(Address)
admin.site.register(Order, OrderAdmin)
