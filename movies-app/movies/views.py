from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request) -> HttpResponse:
    context = {
        'movies': [
            'intersteller',
            'uncharted'
        ]
    }
    return render(request, 'index.html', context)

def about(request) -> HttpResponse:
    return render(request, 'about.html')