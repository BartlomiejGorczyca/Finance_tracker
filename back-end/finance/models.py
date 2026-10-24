from django.conf import settings
from django.db import models

class Category(models.Model):
    type_choices = (("income", "Income"), ("expence", "Expence"))

    name =  models.CharField(max_length=50)
    type = models.CharField(max_length=10, choices=type_choices)
    color = models.CharField(max_length=7)
    icon = models.CharField(max_length=50)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    date = models.DateField()
    description = models.CharField(max_length=255, blank=True)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.amount} for date: ({self.date})"


class Budget(models.Model):
    budget_limit = models.DecimalField(max_digits=12, decimal_places=2)
    month = models.IntegerField()
    year = models.IntegerField()
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.budget_limit} for month: ({self.month})"
