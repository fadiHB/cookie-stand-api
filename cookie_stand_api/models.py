from django.contrib.auth import get_user_model
from django.db import models
# import random

class CookieStand(models.Model):

    location = models.CharField(max_length=256)
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True, blank=True
    )
    description = models.TextField(default="", null=True, blank=True)
    minimum_customers_per_hour = models.IntegerField(default=0)
    maximum_customers_per_hour = models.IntegerField(default=0)
    average_cookies_per_sale = models.FloatField(default=0)
    hourly_sales = models.JSONField(default=list, blank=True)

    # def calc_hourly_sales(self):
    #     return [random.randrange(self.minimum_customers_per_hour, self.maximum_customers_per_hour, 1) * self.average_cookies_per_sale for i in range(15)]


    def __str__(self):
        return self.location


