from django.shortcuts import render
from . import models
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def home_page_views(request):
	media_link = models.SocialMediaLink.objects.all()
	contact = models.Contact.objects.all()
	cuppon_card_list = models.CupponCardPrices.objects.all()
	services = models.Services.objects.all()
	choose_messge_list = models.WhyChooseUSMessage.objects.all()
	services_and_offers = models.ServiceAndOffers.objects.all()
	blogs = models.Blogs.objects.all().order_by('-id')
	if len(blogs) > 3:
		blogs = blogs[:3]
	context = {
		'media_link': media_link,
		'contact':contact,
		'cuppon_card_list': cuppon_card_list,
		'services': services,
		'choose_messge_list': choose_messge_list,
		'services_and_offers': services_and_offers,
		'blogs': blogs
	}
	return render(request, 'website/pages/home.html', context)

def about_views(request):
	media_link = models.SocialMediaLink.objects.all()
	contact = models.Contact.objects.all()
	services = models.Services.objects.all()
	if len(services) > 2:
		services = services[:2]
	choose_messge_list = models.WhyChooseUSMessage.objects.all()
	context = {
		'media_link': media_link,
		'contact':contact,
		'services': services,
		'choose_messge_list': choose_messge_list,
	}
	return render(request, 'website/pages/about.html', context)


def services_views(request):
	media_link = models.SocialMediaLink.objects.all()
	contact = models.Contact.objects.all()
	services = models.Services.objects.all()
	services_and_offers = models.ServiceAndOffers.objects.all()
	context = {
		'media_link': media_link,
		'contact':contact,
		'services': services,
		'services_and_offers': services_and_offers,
	}
	return render(request, 'website/pages/services.html', context)


def contact_views(request):
	media_link = models.SocialMediaLink.objects.all()
	contact = models.Contact.objects.all()
	if request.method == 'POST':
		name = request.POST['name']
		email = request.POST['email']
		phone = request.POST['phone']
		subject = request.POST['subject']
		message = request.POST['message']
		models.ContactMessage.objects.create(
			name = name,
			email = email,
			phone = phone,
			subject = subject,
			message = message
		)

	context = {
		'media_link': media_link,
		'contact':contact,

	}
	return render(request, 'website/pages/contact.html', context)


def blogs_views(request):
	blogs = models.Blogs.objects.all().order_by('-id')
	media_link = models.SocialMediaLink.objects.all()
	contact = models.Contact.objects.all()
	page = request.GET.get('page', 1)
	paginator = Paginator(blogs, 12)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	context = {
		'blogs': blogs,
		'media_link': media_link,
		'contact':contact,
	}

	return render(request, 'website/pages/blogs.html', context)



def blog_details_views(request, id):
	blog = models.Blogs.objects.get(id=id)
	blogs = models.Blogs.objects.all().order_by('-id')
	media_link = models.SocialMediaLink.objects.all()
	contact = models.Contact.objects.all()
	if len(blogs) > 4:
		blogs = blogs[:4]
	context = {
		'blog': blog,
		'blogs': blogs,
		'media_link': media_link,
		'contact':contact,
	}
	return render(request, 'website/pages/blog_details.html', context)




