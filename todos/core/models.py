from django.db import models

# Create your models here.
class Todo(models.Model):
    id=models.BigAutoField(primary_key=True)
    content=models.TextField()
    is_completed=models.BooleanField(default=False)