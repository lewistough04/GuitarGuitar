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
    def get(self, request, genre_name):
        print("get entered")
        try:
            genre = Genre.objects.get(name__iexact=genre_name)
        except Genre.DoesNotExist:
            return Response ({"error": "Genre not found"}, status=404)
        artists = Artist.objects.filter(genre=genre)
        serializer = ArtistSerializer(artists, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        print("post entered")
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

class ArtistGearView(APIView):
    def post(self, request):
        artist_names = request.data.get("artists", [])
        print("Received artist names:", artist_names)

        if artist_names:
            artists = Artist.objects.filter(name__in=artist_names)
            gear_set = Gear.objects.filter(uses__in=artists).distinct()
            serializer = GearSerializer(gear_set, many=True)
                
            print("Returning gear set:", serializer.data)  # Debugging line
            return Response(serializer.data)
        return Response({"error": "No artist names provided"}, status=400)