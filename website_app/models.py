from django.db import models
from django_resized import ResizedImageField
from django.contrib.auth.models import User

class SocialMediaLink(models.Model):
	facebook = models.TextField(blank=True, null=True)
	twitter = models.TextField(blank=True, null=True)
	gmail = models.TextField(blank=True, null=True)
	linkedin = models.TextField(blank=True, null=True)
	
	def __str__(self):
		return 'Social Media Link'

class Contact(models.Model):
	phone = models.CharField(max_length=25, blank=True, null=True)
	whatsapp = models.CharField(max_length=25, blank=True, null=True)
	skype = models.CharField(max_length=25, blank=True, null=True)
	telegram = models.CharField(max_length=25, blank=True, null=True)
	email = models.EmailField(blank=True, null=True)
	address = models.TextField(blank=True, null=True)
	
	def __str__(self):
		return 'Contact'


class CupponCardPrices(models.Model):
	header_title = models.CharField(max_length = 50)
	products_1 = models.CharField(max_length=50)
	price_1 = models.CharField(max_length = 100)
	products_2 = models.CharField(max_length=50)
	price_2 = models.CharField(max_length = 100)
	products_3 = models.CharField(max_length=50)
	price_3 = models.CharField(max_length = 100)

	def __str__(self):
		return self.header_title



class WhyChooseUSMessage(models.Model):
	message = models.TextField()
	def __str__(self):
		return self.message


class Services(models.Model):
	title = models.CharField(max_length=100)
	message = models.TextField()
	image = ResizedImageField(size=[29, 27], upload_to='services/', force_format='PNG')

	def __str__(self):
		return self.title

class ServiceAndOffers(models.Model):
	title = models.CharField(max_length=100)
	message = models.TextField()
	image = ResizedImageField(size=[29, 27], upload_to='services_and_offers/', force_format='PNG')

	def __str__(self):
		return self.title

class Categorys(models.Model):
	category_name = models.CharField(max_length = 100)

	def __str__(self):
		return self.category_name
	

class Blogs(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	image = ResizedImageField(size=[786, 409], upload_to='blog/')
	author = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
	date = models.DateTimeField(auto_now_add = True)
	category = models.ForeignKey(Categorys, on_delete=models.SET_NULL, blank=True, null=True)
		
	def __str__(self):
		return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length = 150)
    email = models.EmailField()
    phone = models.IntegerField()
    subject = models.CharField(max_length = 200)
    message = models.TextField()
    def __str__(self):
        return self.name

	
	


