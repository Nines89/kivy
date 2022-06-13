from django.db import models


class Pizza(models.Model):
    # dichiaro le mie variabili che saranno contenute nel database
    name = models.CharField(max_length=200)  # charfield per le stringhe
    ingredients = models.CharField(max_length=400)
    price = models.FloatField(default=0)
    vegetarian = models.BooleanField(default=False)

    #vedere nell'elenco admin i nomi delle pizze anzichè pizza 1, ...
    def __str__(self):
        return self.name