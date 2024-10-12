from django.test import TestCase
from django.urls import reverse

class APITests(TestCase):
    def test_genre_view(self):
        response = self.client.get(reverse('genres'))
        self.assertEqual(response.status_code, 200)
    
    def test_genre_artist_view(self):
        response = self.client.post(reverse('genre-artists'), {"name": "Rock"}, content_type="application/json")
        self.assertEqual(response.status_code, 200)

    def test_artist_gear_view(self):
        response = self.client.post(reverse('artist-gear'), {"artists": ["Artist1", "Artist2"]}, content_type="application/json")
        self.assertEqual(response.status_code, 200)