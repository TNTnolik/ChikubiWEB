from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from .models import Anime

class Index(View):
    def get(self, request):
        return render(request, "anime/Index.html")


class AnimeListViews(ListView):
    model = Anime
    queryset = Anime.objects.filter(draft=False, draftDelete=False)

class AnimeDetailView(DetailView):
    def get(self, request, slug):
        anime = Anime.objects.get(url=slug)
        return render(request, 'anime/anime_detail.html', {'anime': anime})
