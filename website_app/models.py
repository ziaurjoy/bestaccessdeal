from django.db import models


class SocialMediaLink(models.Model):
	facebook = models.TextField(blank=True, null=True)
	twitter = models.TextField(blank=True, null=True)
	gmail = models.TextField(blank=True, null=True)
	linkedin = models.TextField(blank=True, null=True)
	
	def __str__(self):
		return 'Social Media Link'

class Contact(models.Model):
	phone = models.IntegerField()
	whatsapp_number = models.IntegerField()
	email = models.EmailField()
	open_time = models.CharField(max_length=50)
	address = models.TextField()
	
	def __str__(self):
		return 'Contact'


class CupponCardPrices(models.Model):
	header_title = models.CharField(max_length = 50)
	title_1 = models.CharField(max_length=50)
	title1_p = models.CharField(max_length = 100)
	title_2 = models.CharField(max_length=50)
	title2_p = models.CharField(max_length = 100)
	title_3 = models.CharField(max_length=50)
	title3_p = models.CharField(max_length = 100)

	def __str__(self):
		return self.header_title





