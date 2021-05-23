from rest_framework import serializers

from .models import Joke


class JokeSerializer(serializers.ModelSerializer):
	class Meta:
	
		model = Joke
		fields = ('id','author','body')

class JokeCreateDeatailSerializer(serializers.ModelSerializer):
	author = serializers.ReadOnlyField(source='author.username')
	class Meta:
		model = Joke
		fields = ('id','author','body')




	