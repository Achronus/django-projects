from django.forms import BaseModelForm
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import Trip, Note


class HomeView(TemplateView):
    template_name = 'trip/index.html'


def trips_list(request) -> HttpResponse:
    if request.user.is_authenticated:
        trips = Trip.objects.filter(owner=request.user)
        context = {
            'trips': trips
        }
        return render(request, 'trip/trip_list.html', context)
    return HttpResponseRedirect(reverse('login'))


class TripCreateView(CreateView):
    # templated named 'trip_form.html'
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        # owner field = logged-in user
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TripDetailView(DetailView):
    # template named 'trip_detail.html'
    model = Trip

    def get_context_data(self, **kwargs) -> dict:
        """Add notes to Trip object."""
        context = super().get_context_data(**kwargs)
        print(context)
        trip = context['object']
        notes = trip.notes.all()
        context['notes'] = notes
        return context


class TripUpdateView(UpdateView):
    # No template needed - sends 'PUT' request to 'trip_list'
    model = Trip
    success_url = reverse_lazy('trip-list')
    fields = ['city', 'country', 'start_date', 'end_date']


class TripDeleteView(DeleteView):
    # No template needed - sends 'POST' request to 'trip_list'
    model = Trip
    success_url = reverse_lazy('trip-list')



class NoteDetailView(DetailView):
    # template named 'note_detail.html'
    model = Note


class NoteListView(ListView):
    # template named 'note_list.html'
    model = Note
    
    def get_queryset(self):
        queryset = Note.objects.filter(trip__owner=self.request.user)
        return queryset


class NoteCreateView(CreateView):
    # template named 'note_form.html'
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"

    def get_form(self):
        form = super().get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        print(form.fields['trip'])
        form.fields['trip'].queryset = trips
        return form


class NoteUpdateView(UpdateView):
    # No template needed - sends 'PUT' request to 'note_list'
    model = Note
    success_url = reverse_lazy('note-list')
    fields = "__all__"

    def get_form(self):
        form = super().get_form()
        trips = Trip.objects.filter(owner=self.request.user)
        print(form.fields['trip'])
        form.fields['trip'].queryset = trips
        return form


class NoteDeleteView(DeleteView):
    # No template needed - sends 'POST' request to 'note_list'
    model = Note
    success_url = reverse_lazy('note-list')
