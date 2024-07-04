from django.urls import path
from .views import homepage, movie_details, delete_movie

urlpatterns=[
    path('', homepage, name="homepage"),
    path("movie_details/<int:movie_id>/",movie_details, name="movie_details"),
    path("delete_movie/<int:movie_id>", delete_movie, name="delete_movie")
    
]