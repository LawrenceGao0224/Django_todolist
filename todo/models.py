from django.db import models

class Todoitem(models.Model):
    content = models.TextField()