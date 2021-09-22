from django.db import models
from django.utils import timezone

class Blog(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date= models.DateTimeField(default=timezone.now)
	author=models.CharField(max_length=100)
	image= models.ImageField(default='default.jpg', upload_to='blog_pics')
	def  __str__(self):
		return self.title

class Gallery(models.Model):
	title = models.CharField(max_length=100)
	spcat = models.CharField(blank=True,max_length=100)
	date= models.DateTimeField(default=timezone.now)
	description = models.TextField(blank=True)
	image1= models.ImageField(default='default.jpg', upload_to='gallery_pics')
	image2= models.ImageField(default='default.jpg', upload_to='gallery_pics')
	image3= models.ImageField(default='default.jpg', upload_to='gallery_pics')

	
	

	def  __str__(self):
		return self.title

class Service(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField(blank=True)
	image= models.ImageField(default='default.jpg', upload_to='Service_pics')
	image2= models.ImageField(default='default.jpg', upload_to='Service_pics')
	image3= models.ImageField(default='default.jpg', upload_to='Service_pics')
	
	
	

	def  __str__(self):
		return self.title
# Create your models here.
