from django.db import models

# Create your models here.
class Todos(models.Model):
    title= models.CharField(max_length=100)
    text = models.TextField()
    type = "Todo"
    def __str__(self) -> str:
        return self.title