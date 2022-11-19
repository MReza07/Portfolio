from django.shortcuts import render
from .models import my_skill, contact_info


def home(request):
    items = my_skill.objects.all()
    title = 'Wel come to REZA IT'
    description = 'it is my personal portfolio web site '
    context = {
        'title': title,
        'description': description,
        'data': items
    }
    return render(request, 'index.html', context)


def about(request):
    title = 'About '
    aboutdese = 'Looking for a promising & challenging career which will enable me to provide best of my technical, analytical & professional skills'
    return render(request, 'about.html', {'title': title, 'aboutdese': aboutdese})


def contact(request):
    title = 'Contact '
    contactdese = 'Please contact with me for any requirement'
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        my_data = contact_info(cname=name, cemail=email, csubject=subject, cmessage=message)
        my_data.save()

    return render(request, 'contact.html', {'title': title, 'contactdese': contactdese})
