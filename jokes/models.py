from django.db import models
from django.contrib.auth.models import User

class Joke(models.Model):
	author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='jokes') 
	body = models.TextField()

	def __str__(self):
		return self.body[:6]
# Create your models here.
