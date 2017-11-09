from django.db import models

# Create your models here.

class Things(models.Model):
	name = models.CharField(max_length=50)
	id = models.CharField(max_length=20,primary_key=True)
	status = models.TextField(default=0)
