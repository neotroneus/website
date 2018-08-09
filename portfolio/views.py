from django.views import generic
from .models import Website



class IndexView(generic.ListView):
    template_name = 'portfolio/index.html'
    context_object_name = 'all_projects'

    def get_queryset(self):
        return Website.objects.all()