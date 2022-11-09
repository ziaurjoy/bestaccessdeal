from django.urls import path
from . import views
urlpatterns = [
    path('', views.home_page_views, name='home'),
    path('about', views.about_views, name='about'),
    path('services', views.services_views, name='services'),
    path('contact', views.contact_views, name='contact'),
    path('blog', views.blogs_views, name='blogs'),
    path('blog/<int:id>', views.blog_details_views, name='blog-details')
]