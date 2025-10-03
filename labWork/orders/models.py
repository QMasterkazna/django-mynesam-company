from django.db import models
from django.conf import settings
# Create your models here.

class Order(models.Model):
    SERVICE_CHOICES = [
        ("general", "Общий клининг"),
        ("deep", "Генеральная уборка"),
        ("post_building","Послестроительная уборка"),
        ("dry_clean","Химчистка ковров и мебели"),
    ]
    PAYMENT_CHOICES = [
        ("cash", "Наличные"),
        ("card", "Банковская карта")
    ]
    STATUS_CHOICES = [
        ("new","Новая заявка"),
        ("in_progress", "В работе"),
        ("done","Услуга оказана"),
        ("cancelled", "Отменено")
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.CharField("Адрес", max_length=255)
    contact_phone = models.CharField("Телефон", max_length=20)
    service_type = models.CharField("Вид услуги", max_length=50, choices=SERVICE_CHOICES)
    preferred_datetime = models.DateTimeField("Желаемая дата и время")
    payment_type = models.CharField("Тип оплаты", max_length=20, choices=PAYMENT_CHOICES)
    status = models.CharField("Статус", max_length=20, choices=STATUS_CHOICES, default="new")
    cancel_reason = models.CharField("Причина отмены", max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} — {self.service_type} — {self.status}"