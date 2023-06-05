from django.db import models


# Создаем класс Поставщика
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'trade_network'  # Название приложения, к которому относится модель


# Создаем класс Сети электроники с определением уровня
class ElectronicsNetwork(models.Model):
    LEVEL_CHOICES = (
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    )

    name = models.CharField(max_length=100)
    contact_email = models.EmailField()
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_number = models.CharField(max_length=20)
    products = models.ManyToManyField('Product')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    debt = models.DecimalField(max_digits=10, decimal_places=2)
    level = models.IntegerField(choices=LEVEL_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)


# Создаем класс Продукта
class Product(models.Model):
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    release_date = models.DateField()


# Создаем класс действия администратора
class AdminAction(models.Model):
    network = models.ForeignKey(ElectronicsNetwork, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=100)
    executed_at = models.DateTimeField(auto_now_add=True)
