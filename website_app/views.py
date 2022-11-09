from django.shortcuts import render
from . import models
# Create your views here.

def home_page_views(request):
  media_link = models.SocialMediaLink.objects.all()
  contact = models.Contact.objects.all()
  cuppon_card_list = models.CupponCardPrices.objects.all()
  context = {
    'media_link': media_link,
    'contact':contact,
    'cuppon_card_list': cuppon_card_list,
  }
  return render(request, 'website/pages/home.html', context)


