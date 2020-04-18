from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Anime
from .forms import ReviewsForm


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


class AddReview(View):

    def post(self, request, slug):
        form = ReviewsForm(request.POST)
        anime = Anime.objects.get(url=slug)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.anime = anime
            form.user = request.user
            form.save()
        return redirect(f"/anime/{slug}")
