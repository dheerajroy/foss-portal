from django.urls import path
from .views import CoreTeamMembersList

urlpatterns = [
    path('', CoreTeamMembersList.as_view(), name='core-team-members'),
]
