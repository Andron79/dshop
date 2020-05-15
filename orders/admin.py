from django.contrib import admin
from .models import Order, OrderItem
from accounts.models import UserProfile


# class UserProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'orders']
#
#
# class UserProfileInline(admin.TabularInline):
#     model = UserProfile
#     readonly_fields = ('user',)
#     extra = 1


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'phone', 'city', 'paid',
                    'created', 'updated']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    readonly_fields = ('id', 'first_name', 'last_name', 'email',
                       'address', 'phone', 'city',)
    #
    # def auth_profile(self, obj):
    #     return obj.users.orders
    #
    # auth_profile.short_description = "Users orders"


admin.site.register(Order, OrderAdmin)

#
#
# admin.site.register(UserProfile, UserProfileAdmin)
