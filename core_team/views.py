from django.views.generic import ListView
from .models import CoreTeamMember


class CoreTeamMembersList(ListView):
    model = CoreTeamMember
    template_name = 'core-team.html'
    context_object_name = 'members'
