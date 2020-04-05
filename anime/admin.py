from django.contrib import admin
from .models import Profile, Anime, Genre, Category, Studio, Series, Frame, Reviews


class ProfileAdmin(admin.ModelAdmin):
    pass


class AnimeAdmin(admin.ModelAdmin):
    pass


class StudioAdmin(admin.ModelAdmin):
    pass


class GenreAdmin(admin.ModelAdmin):
    pass


class CategoryAdmin(admin.ModelAdmin):
    pass


class SeriesAdmin(admin.ModelAdmin):
    pass


class FrameAdmin(admin.ModelAdmin):
    pass


class ReviewsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile, ProfileAdmin)
admin.site.register(Anime, AnimeAdmin)
admin.site.register(Series, SeriesAdmin)
admin.site.register(Frame, FrameAdmin)
admin.site.register(Studio, StudioAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Reviews, ReviewsAdmin)
