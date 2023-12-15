from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .models import Event, Registration, Feedback
from .forms import RegistrationForm, FeedbackForm


class EventListView(ListView):
    queryset = Event.objects.filter(publish=True)
    template_name = 'events.html'
    context_object_name = 'events'


class EventDetailView(DetailView):
    model = Event
    template_name = 'event.html'
    context_object_name = 'event'


class RegistrationCreateView(CreateView):
    model = Registration
    form_class = RegistrationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.event_id = self.kwargs.get('pk')
        return super().form_valid(form)


class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = 'feedback.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.event_id = self.kwargs.get('pk')
        return super().form_valid(form)
