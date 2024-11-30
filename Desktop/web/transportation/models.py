from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Client(models.Model):
    name = models.TextField("ФИО")
    email = models.TextField("Электронная почта")
    phone = models.TextField("Номер телефона")
    picture = models.ImageField("Изображение", null=True, upload_to="clients")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", null=True)
    
    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
    
    def __str__(self) -> str:
        return self.name
    
        
class Flight(models.Model):
    flight_number = models.CharField("Номер рейса", max_length=10)
    departure = models.CharField("Пункт отправления", max_length=100)
    destination = models.CharField("Пункт назначения", max_length=100)
    departure_time = models.DateTimeField("Время отправления")
    arrival_time = models.DateTimeField("Время прибытия")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", null=True)    
    
    class Meta:
        verbose_name = "Рейс"
        verbose_name_plural = "Рейсы"

    def __str__(self) -> str:
        return self.flight_number
    
class Ticket(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name="Рейс")
    seat_number = models.CharField("Номер места", max_length=5)
    purchase_date = models.DateTimeField("Дата покупки", auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", null=True)
        
    class Meta:
        verbose_name = "Билет"
        verbose_name_plural = "Билеты"

    def __str__(self) -> str:
        return self.seat_number
    
class Baggage(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, verbose_name="Билет")
    weight = models.DecimalField("Вес (кг)", max_digits=5, decimal_places=2)
    baggage_type = models.CharField("Тип багажа", max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", null=True)   
    
    class Meta:
        verbose_name = "Багаж"
        verbose_name_plural = "Багажи"

    def __str__(self) -> str:
        return self.baggage_type
    
class Airplane(models.Model):
    tail_number = models.CharField("Бортовой номер", max_length=10, unique=True)
    model = models.CharField("Модель", max_length=50)
    capacity = models.IntegerField("Вместимость")
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, verbose_name="Рейс")
    picture = models.ImageField("Изображение", null=True, upload_to="airplane")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь", null=True) 
    class Meta:
        verbose_name = "Самолет"
        verbose_name_plural = "Самолеты"
        
    def __str__(self) -> str:
        return self.tail_number    
    