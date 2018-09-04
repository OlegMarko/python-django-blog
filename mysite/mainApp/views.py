from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': [
        'Lorem ipsum dolor sit amet, consectetur adipisicing elit. A minima optio provident velit? Doloremque, praesentium!',
        '(098) 123 45 67'
    ]})
