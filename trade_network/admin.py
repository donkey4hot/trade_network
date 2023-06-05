from django.contrib import admin
from .models import Supplier, ElectronicsNetwork, Product, AdminAction


# Регистрируем модель Supplier
@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'country', 'city', 'street', 'house_number', 'created_at')


# Регистрируем модель ElectronicsNetwork
@admin.register(ElectronicsNetwork)
class ElectronicsNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'contact_email', 'country', 'city', 'street', 'house_number', 'supplier', 'debt', 'level', 'created_at')
    list_filter = ('city',)  # Возможность фильтрации объектов по полю "city"
    actions = ['clear_debt']  # Добавляем действие "clear_debt" для выбранных объектов

    def clear_debt(self, queryset):
        queryset.update(debt=0)  # Метод для обновления значения поля "debt" у выбранных объектов

    clear_debt.short_description = 'Очистить задолженность'  # Описание действия "clear_debt"


# Регистрируем модель Product
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'model', 'release_date')


# Регистрируем модель AdminAction
@admin.register(AdminAction)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('network', 'action_type', 'executed_at')
