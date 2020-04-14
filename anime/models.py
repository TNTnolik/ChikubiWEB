from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from datetime import date


# TODO: Rating
def user_directory_path(instance, filename):
    return 'avatars/{0}.{1}'.format(instance.user.username, filename.split('.')[-1])


def anime_directory_path(instance, filename):
    return 'anime/{0}/{1}'.format(instance.originalName, filename)


def studio_directory_path(instance, filename):
    return 'studio/{0}.{1}'.format(instance.name, filename.split('.')[-1])


def frame_directory_path(instance, filename):
    return 'anime/frame/{0}/{1}.{2}'.format(instance.anime, instance.name, filename.split('.')[-1])


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False)
    nick_name = models.CharField('Ник', max_length=200, null=True, blank=True)
    first_name = models.CharField('Имя', max_length=200, null=True, blank=True)
    avatar = models.ImageField('Аватар', upload_to=user_directory_path, default='avatars/def.svg')
    description = models.TextField('Описание', null=True, blank=True)
    descriptionBool = models.BooleanField('Видено ли описание', default=False)
    year = models.DateField('Возраст', null=True, blank=True)
    fraza = models.CharField('Любимая фраза', max_length=300, null=True, blank=True)
    frazaBool = models.BooleanField('Видена ли фраза', default=True)

    def __str__(self):
        return f"{self.user.username}"

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, nick_name=instance.username)


post_save.connect(create_profile, sender=User)


def update_profile(sender, instance, created, **kwargs):
    if created == False:
        instance.profile.save()


post_save.connect(update_profile, sender=User)


class Studio(models.Model):
    name = models.CharField('Название', max_length=200, null=False, blank=False)
    poster = models.ImageField('Постер', upload_to=studio_directory_path, default='avatars/def.svg')
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Студия"
        verbose_name_plural = "Студии"


class Genre(models.Model):
    name = models.CharField('Название', max_length=200, null=False, blank=False)
    description = models.TextField('Описание', null=True, blank=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class Category(models.Model):
    name = models.CharField('Название', max_length=160, null=False, blank=False)
    description = models.TextField('Описание', null=True, blank=True)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Anime(models.Model):
    name = models.CharField('Название', max_length=300, null=False, blank=False)
    originalName = models.CharField('Оригинальное название', max_length=300, null=False, blank=False)
    premiere = models.DateField("Дата примьеры", default=date.today)
    description = models.TextField('Описание', null=True, blank=True)
    poster = models.ImageField('Постер', upload_to=anime_directory_path, default='avatars/def.svg')
    background = models.ImageField('Фон', upload_to=anime_directory_path, default='avatars/def.svg')
    studio = models.ForeignKey(Studio, on_delete=models.SET_NULL, null=True)
    voise = models.ManyToManyField(User, related_name='voiser')
    translate = models.ManyToManyField(User, related_name='translate')
    timer = models.ForeignKey(User, related_name='Timer', null=True, on_delete=models.SET_NULL)
    genres = models.ManyToManyField(Genre, related_name='genres')
    categorys = models.ManyToManyField(Category, related_name='categorys')
    url = models.SlugField(max_length=160, unique=True)
    draft = models.BooleanField('Черновик', default=False)
    draftDelete = models.BooleanField('Удалено для модераторов', default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Аниме"


class Series(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    number = models.PositiveSmallIntegerField('Номер серии')
    name = models.CharField('Название серии', max_length=160)
    url = models.URLField('Ссылка на видео')

    def __str__(self):
        return '{0} Серия №{1}'.format(str(self.anime), self.number)

    class Meta:
        verbose_name = "Серия"
        verbose_name_plural = "Серии"


class Frame(models.Model):
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    name = models.CharField('Название', max_length=160)
    description = models.TextField('Описание', null=True, blank=True)
    img = models.ImageField('Кадр', upload_to=frame_directory_path)

    def __str__(self):
        return '{0} | Кадр: {1}'.format(str(self.anime), self.name)

    class Meta:
        verbose_name = 'Кадр из аниме'
        verbose_name_plural = 'Кадры из аниме'


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self', verbose_name='Родитель', blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.user.username} - {self.anime}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Rating(models.Model):
    RATING =[
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    rating = models.CharField(max_length=2, choices=RATING)

    def __str__(self):
        return f"{self.anime} - оценка {self.rating}"

    class Meta:
        verbose_name = 'Рэйтинг'
        verbose_name_plural = 'Рэйтинг'
