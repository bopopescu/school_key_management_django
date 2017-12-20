from django.views.generic import ListView, DetailView
from human.models import Human


class HumanListView(ListView):
    model = Human


class HumanDetailView(DetailView):
    model = Human
