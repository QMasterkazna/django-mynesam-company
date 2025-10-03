from django.contrib import admin
from .models import Order

# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'service_type', 'address', 'preferred_datetime', 'payment_type', 'status', 'created_at')
    list_filter = ('status', 'service_type', 'payment_type')
    search_fields = ('user__username', 'address', 'contact_phone')
    readonly_fields = ('created_at',)