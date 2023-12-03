from django.shortcuts import render, HttpResponse, HttpResponseRedirect, get_object_or_404, redirect
from django.urls import reverse

from .models import Link
from .forms import LinkForm

# Create your views here.
def index(request) -> HttpResponse:
    links: list = Link.objects.all()
    context = {
        'links': links
    }
    return render(request, 'index.html', context)


def root_link(request, link_slug: str) -> HttpResponseRedirect:
    link = get_object_or_404(Link, slug=link_slug)
    link.increment_clicks()

    return redirect(link.url)


def add_link(request) -> HttpResponse:
    if request.method == 'POST':
        # Form has data
        form = LinkForm(request.POST)
        
        if form.is_valid():
            # Save data & return to homepage
            form.save()
            return redirect(reverse('home'))
    else:
        form = LinkForm()

    context = {
        'form': form
    }
    return render(request, 'create.html', context)
