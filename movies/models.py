from django.utils import timezone

# Create your models here.
from django.db import models
# from accounts.models import SubUser


class Director(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Actor(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Feature(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Degree(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Movie(models.Model):
    name = models.CharField(max_length=50)

    video_file = models.FileField(upload_to=f'media/movie/{name}/video')
    sample_video_file = models.FileField(upload_to=f'media/movie/{name}/sample_video')

    directors = models.ManyToManyField(Director, related_name='movie_directors')
    actors = models.ManyToManyField(Actor, related_name='movie_actors')
    feature = models.ManyToManyField(Feature, related_name='movie_feature')
    author = models.ManyToManyField(Author, related_name='movie_author')
    degree = models.ForeignKey(Degree, on_delete=models.SET_NULL, related_name='movie_degree', null=True)
    genre = models.ManyToManyField(Genre, related_name='movie_genre')

    production_date = models.DateField(default=timezone.now)
    uploaded_date = models.DateField(default=timezone.now)

    synopsis = models.TextField()
    running_time = models.CharField(max_length=10)
    view_count = models.PositiveIntegerField(default=0)

    logo_image_path = models.TextField(default="")
    horizontal_image_path = models.TextField(default="")
    vertical_image = models.ImageField(upload_to=f'media/movie/{name}/horizontal')
    circle_image = models.ImageField(upload_to=f'media/movie/{name}/circle')

    def __str__(self):
        return self.name


class MovieContinue(models.Model):
    movie_id = models.ForeignKey(Movie, related_name='movie_continue', on_delete=models.CASCADE)
    sub_user_id = models.ForeignKey('accounts.SubUser', related_name='movie_continue', on_delete=models.CASCADE)
    to_be_continue = models.TimeField()

    def __str__(self):
        return str(self.movie_id) + " " + str(self.sub_user_id) + " " + str(self.to_be_continue)

    # 영화 국적 - 완
    # 이미지필드 최소 3개 - 완
    # 세로 영상 - 보류
    # 미리보기 동영상(마우스 오버를 하면 요청을 받아 보내기) - 완
    # 이미지 가로,세로요청을 헤더로 T/F를 넣어 보냄 - ?
    # 영화 이어보기(멈췄던) 시간 - ?
