from rest_framework import viewsets, filters
from .models import Supplier
from .serializers import SupplierSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()  # Запрос для получения всех объектов модели Supplier
    serializer_class = SupplierSerializer  # Сериализатор, используемый для преобразования данных Supplier
    filter_backends = [filters.SearchFilter]  # Указание фильтров, применяемых к запросам
    search_fields = ['country']  # Поля, по которым можно выполнять поиск
