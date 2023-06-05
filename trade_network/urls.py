from django.contrib import admin
from django.urls import path

from trade_network import views

urlpatterns = [
    path('admin/', admin.site.urls),  # URL-шаблон для административного интерфейса Django
    path('api/suppliers/', views.SupplierViewSet.as_view({'get': 'list'}), name='supplier-list'),  # URL-шаблон для API поставщиков
]
