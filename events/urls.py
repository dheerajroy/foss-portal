from django.urls import path
from .views import EventListView, EventDetailView, RegistrationCreateView, FeedbackCreateView

urlpatterns = [
    path('', EventListView.as_view(), name='events'),
    path('<int:pk>/', EventDetailView.as_view(), name='event'),
    path('<int:pk>/register/', RegistrationCreateView.as_view(), name='register'),
    path('<int:pk>/feedback/', FeedbackCreateView.as_view(), name='feedback'),
]
