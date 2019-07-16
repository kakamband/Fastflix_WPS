from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import JsonResponse
from django.views import View
from rest_framework import generics
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.settings import api_settings

from movies.models import Movie
from .models import User
from .serializer import UserCreateSerializer


class CreateLike(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            if 'movie_id' in kwargs['movie_id']:
                parent_user = request.user
                sub_user = parent_user.sub_user.all().filter(logined=True).get()
                movie = Movie.objects.get(pk=kwargs['movie_id'])
                if sub_user in movie.likes.all():
                    movie.likes.remove(sub_user)
                    return JsonResponse({'data': 'remove'})
                else:
                    movie.likes.add(sub_user)
                    return JsonResponse({'data': 'add'})


# 회원가입 API
class UserCreate(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # 넘어온 데이터값이 유효하다면
        # serializer의 create 함수를 실행시킨다
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        # 회원가입된 유저의 id값을 가져온다
        created_user_id = serializer.data['id']

        # 가져온 id값을 바탕으로 토큰값을 가져온다
        context = {
            'Token': Token.objects.get(user_id=created_user_id).key
        }

        # serializer.data는 클래스의 속성이므로 변경할수 없다
        # 새로운 dict을 만들고 context를 추가한 다음에 serializer.data를 추가한다
        new_dict = context
        new_dict.update(serializer.data)

        return Response(new_dict, status=status.HTTP_201_CREATED, headers=headers)

    def perform_create(self, serializer):
        serializer.save()

    def get_success_headers(self, data):
        try:
            return {'Location': str(data[api_settings.URL_FIELD_NAME])}
        except (TypeError, KeyError):
            return {}


# 회원가입이 되면 회원가입 완료 시그널을 받아 토큰을 생성하고 저장한다
@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

# def create_user(request):
#     if request.method == "POST":
#         form = UserCreateForm(request.POST)
#         if form.is_valid():
#             user = User(username=form.data['name'], password=form.data['password'])
#             user.save()
#             return JsonResponse('success')
#
#     else:
#         form = UserCreateForm()
#         return JsonResponse(form)
