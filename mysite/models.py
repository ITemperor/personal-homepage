from django.db import models

class Image(models.Model):
	img=models.ImageField(upload_to = './img')

class Text(models.Model):
	text=models.CharField(max_length=1024)
