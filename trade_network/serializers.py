from rest_framework import serializers
from .models import Supplier


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier  # Определение модели, которая будет сериализована
        fields = '__all__'  # Включение всех полей модели в сериализацию
        read_only_fields = ['debt']  # Установка поля "debt" только для чтения
