from django.shortcuts import render
# Create your views here.


def landing_page(request):
    template = 'index.html'
    return render(request, template)

def sevice(request):
    template = 'service.html'
    return render(request, template)