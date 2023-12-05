from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()
    desc = models.TextField()

    def __str__(self) -> str:
        return f'{self.name} at £{self.price}'
    
