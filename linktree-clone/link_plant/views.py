from django.shortcuts import get_object_or_404, render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Profile, Link


# Classes replace the need for function declarations
class LinkListView(ListView):
    # Looks for template called {model}_list.html
    # In our case, 'link_list.html'
    model = Link


class LinkCreateView(CreateView):
    model = Link
    fields = "__all__"
    success_url = reverse_lazy("link-list")  # redirects to

    # Requires a: 
    # - template {model}_form.html -> 'link_form.html'


class LinkUpdateView(UpdateView):
    # Equivalent to:
    # - Creating a form
    # - Checking for a get or put request
    # - Either, render form or update and save DB
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')

    # Shares same template as 'LinkCreateView' (link_form.html)


class LinkDeleteView(DeleteView):
    # Equivalent to:
    # - Accepting an id/pk of an object
    # - Querying DB for the object
    # - Checking it it exists, then deleting object (if true)
    # - + returning template or forwarding to a url
    model = Link
    success_url = reverse_lazy('link-list')

    # Requires a:
    # - template {model}_confirm_delete.html -> 'link_confirm_delete.html'


def profile_view(request, slug: str) -> HttpResponse:
    profile = get_object_or_404(Profile, slug=slug)
    links = profile.links.all()
    context = {
        'profile': profile,
        'links': links
    }
    return render(request, 'link_plant/profile.html', context)
