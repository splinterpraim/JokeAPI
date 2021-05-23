from django.urls import path

from .views import ListJoke, DetailJoke,GenerateJoke,CreateJoke
urlpatterns = [
	path('generate/',GenerateJoke.as_view()),
	path('create/',CreateJoke.as_view()),
	path('<int:pk>/',DetailJoke.as_view()),
	path('',ListJoke.as_view()),
]