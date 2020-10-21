from django.shortcuts import render
from django.http import HttpResponse
from services.models import Service, Service_heading, Solution
from contacts.models import Contact_heading, Address
from home.models import Slide, Page
from about.models import About
from django.contrib import messages, auth





def index(request):
    abouts = About.objects.order_by('date_posted').filter(is_published=True)[:1]
    slides = Slide.objects.order_by('date_posted').filter(is_published=True)
    services = Service.objects.order_by('date_posted').filter(is_published=True)[:8]
    solutions = Solution.objects.order_by('date_posted').filter(is_published=True)[:1]
    headings = Service_heading.objects.order_by('date_posted').filter(is_published=True)[:1]
    heading = Contact_heading.objects.order_by('date_posted').filter(is_published=True)[:1]
    addresss = Address.objects.all() 
    f1_pages = Page.objects.all().filter(is_footer_1=True)[:3]
    f2_pages = Page.objects.all().filter(is_footer_2=True)[:3]
    f3_pages = Page.objects.all().filter(is_footer_3=True)[:3]

    context = {  
        'abouts':abouts,
        'slides':slides,   
        'services':services, 
        'heading':heading,
        'headings':headings,
        'solutions':solutions,
        'addresss':addresss,
        'f1_pages':f1_pages,
        'f2_pages':f2_pages,
        'f3_pages':f3_pages,
    }
    return render(request, 'pages/index.html', context)



