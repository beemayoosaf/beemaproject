from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Category, Collar, Dealer, Franchise_Type, Franchisee, Service_Type, ServiceProvider, ServiceRegister, Subcategory, User,Country_Codes
# Register your models here.

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'is_staff', 'is_superuser')
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(User, UserAdmin)
admin.site.register(Country_Codes)


class ServiceRegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'service_provider', 'title', 'description', 'gstcode', 
                    'category', 'subcategory', 'license', 'image', 'accepted_terms', 'collar','available_lead_balance')

# Register the model with the custom admin class
admin.site.register(ServiceRegister, ServiceRegisterAdmin)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')

# Register the model with the custom admin class
admin.site.register(Category, CategoryAdmin)

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','service_type','status')

# Register the model with the custom admin class
admin.site.register(Subcategory, SubCategoryAdmin)


@admin.register(Franchisee)
class FranchiseeAdmin(admin.ModelAdmin):
    list_display = ('custom_id', 'user', 'type', 'community_name', 'revenue', 'dealers', 'service_providers', 'status', 'valid_from', 'valid_up_to')  # Columns to display
    list_filter = ('status', 'type', 'valid_from', 'valid_up_to')  # Filters for the sidebar
    search_fields = ('custom_id', 'user__username', 'community_name')  # Fields to search by
    ordering = ('valid_from',)  # Default ordering by 'valid_from' field

@admin.register(Dealer)
class DealerAdmin(admin.ModelAdmin):
    list_display = ('custom_id', 'user', 'franchisee', 'service_providers', 'status', 'verification_id')  # Columns to display
    list_filter = ('status', 'franchisee')  # Filters for the sidebar
    search_fields = ('custom_id', 'user__username', 'franchisee__custom_id')  # Fields to search by
    ordering = ('user',)  # Default ordering by 'user'

@admin.register(Franchise_Type)
class FranchiseTypeAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('name', 'amount', 'currency')

    # Fields to allow searching
    search_fields = ('name', 'details', 'currency')

    # Default ordering (by 'name' and 'amount')
    ordering = ('name', 'amount')

    # Optionally, you can make `list_filter` for easy filtering
    list_filter = ('currency',)


class CollarAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lead_quantity','amount')

# Register the model with the custom admin class
admin.site.register(Collar, CollarAdmin)

class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','details')

# Register the model with the custom admin class
admin.site.register(Service_Type, ServiceTypeAdmin)

@admin.register(ServiceProvider)
class ServiceProviderAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('custom_id', 'user', 'dealer', 'franchisee', 'payout_required', 'status', 'verification_by_dealer')

    # Fields to allow searching
    search_fields = ('custom_id', 'user__username', 'dealer__custom_id', 'franchisee__custom_id', 'status')

    # Default ordering (by 'user' and 'custom_id')
    ordering = ('user', 'custom_id')

    # Optionally, you can make `list_filter` for easy filtering
    list_filter = ('status', 'payout_required', 'verification_by_dealer')

