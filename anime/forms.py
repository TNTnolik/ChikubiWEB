from django import forms

from .models import Reviews, Rating, AnimeList


class ReviewsForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = {"text"}


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = {"rating"}

#TODO: Доделать рэйтинг и статус