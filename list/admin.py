from list.models import ShoppingList,Item
from django.contrib import admin

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1

class ShoppingListAdmin(admin.ModelAdmin):
    fieldsets = [
        ('none', {'fields': ['name']})
        ]
    inlines = [ItemInline]
    

admin.site.register(ShoppingList, ShoppingListAdmin)
