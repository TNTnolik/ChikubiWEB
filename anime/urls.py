from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view()),
    path('list/', AnimeListViews.as_view())
]