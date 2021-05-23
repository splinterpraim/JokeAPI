from rest_framework import generics
from rest_framework.views import APIView 
from rest_framework.response import Response
from .serializers import JokeSerializer, JokeCreateDeatailSerializer
from .models import Joke
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAuthenticated
import requests as rq


class ListJoke(generics.ListAPIView):
	"""Вывод списка моих шуток"""
	permission_classes = [IsAuthenticated,IsAuthorOrReadOnly,]
	serializer_class = JokeSerializer
	def get_queryset(self):
		user = self.request.user
		return user.jokes.all()

class CreateJoke(generics.CreateAPIView):
	"""Создать шутку"""
	permission_classes = [IsAuthenticated]
	serializer_class = JokeCreateDeatailSerializer

	def perform_create(self,serializer):
		serializer.save(author=self.request.user
			)
	def get_queryset(self):
		user = self.request.user
		return user.jokes.all()

class DetailJoke(generics.RetrieveUpdateDestroyAPIView):
	"""Детальный просмотр, обнавление и удаление шутки"""
	serializer_class = JokeCreateDeatailSerializer
	def get_queryset(self):
		user = self.request.user
		return user.jokes.all()


class GenerateJoke(APIView):
	"""Сгенерировать шутку"""
	def get(self,request):
		user = request.user
		body = rq.get('https://geek-jokes.sameerkumar.website/api').json()
		joke = Joke.objects.create(author=user,body=body)
		serializer = JokeSerializer(joke)
		return Response(serializer.data)
# Create your views here.
