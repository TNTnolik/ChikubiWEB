from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view()),
    path('anime/<slug:slug>/', AnimeDetailView.as_view(), name="Anime_Detail"),
    path('list/', AnimeListViews.as_view(), name="AnimeList"),
    path('review/<slug:slug>/', AddReview.as_view(), name='add_review')
]