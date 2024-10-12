from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response


class GenreView(APIView):
    def get(self, request):
        output = [{"name": output.name}
                   for output in Genre.objects.all()]
        return Response(output)
    
#a class to get artists for certain genre
class GenreArtistView(APIView):
    def get(self, request):
        output = [{"name": output.name} for output in Artist.objects.all()]
        return Response(output)
    
    def post(self, request):
        genre_name = request.data.get("name", None)
        if genre_name:
            try:
                print(genre_name)
                genre = Genre.objects.get(name=genre_name)

            except Genre.DoesNotExist:
                return Response({"error": "Genre not found"}, status=404)
        
            artists = Artist.objects.filter(genre=genre)
            serializer = ArtistSerializer(artists, many = True)
            return Response(serializer.data)
        return Response({"error": "Invalid genre"}, status=400)