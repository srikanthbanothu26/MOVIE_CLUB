from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
import requests
from django.contrib.auth.decorators import login_required

@login_required
def homepage(request):
    if request.method == "POST":
        movieName = request.POST.get("movieName").strip()
        apiKey = "28f9e296"  
        
        movie = Movie.objects.filter(Title__iexact=movieName).first()
        
        if movie:
            return render(request, "index.html", {"movie": movie})
        
        apiUrl = f"http://www.omdbapi.com/?t={movieName}&apikey={apiKey}"
        
        try:
            resp = requests.get(apiUrl)
            resp.raise_for_status()
            data = resp.json()
            
            if data.get("Response") == "True":
                movie = Movie(
                    Title=data.get("Title", "N/A"),
                    Year=data.get("Year", "N/A"),
                    Rated=data.get("Rated", "N/A"),
                    Released=data.get("Released", "N/A"),
                    Runtime=data.get("Runtime", "N/A"),
                    Genre=data.get("Genre", "N/A"),
                    Director=data.get("Director", "N/A"),
                    Writer=data.get("Writer", "N/A"),
                    Actors=data.get("Actors", "N/A"),
                    plot=data.get("Plot", "N/A"),
                    Poster=data.get("Poster", "N/A"),
                    ImdbRating=data.get("imdbRating","N/A"),
                    ImdbVotes=data.get("imdbVotes", "N/A").replace(",", ""),
                    BoxOffice=data.get("BoxOffice", "N/A"),
                    Language=data.get("Language", "N/A"),
                    Awards=data.get("Awards", "N/A"),
                    Country=data.get("Country", "N/A"),
                )
                movie.save()
                return render(request, "index.html", {"movie": movie})
            else:
                return render(request, "index.html", {"error": data.get("Error", "Unknown error")})
        except requests.exceptions.RequestException as e:
            return render(request, "index.html", {"error": "Unable to fetch data from OMDB API. Exception: " + str(e)})
    
    movies=Movie.objects.all()
    unique_movies = []
    titles = set()
    for m in movies:
        if m.Title not in titles:
            titles.add(m.Title)
            unique_movies.append(m)
            
    return render(request, "index.html", {"movies": unique_movies})
 
@login_required   
def movie_details(request, movie_id):
    movie =get_object_or_404(Movie, id=movie_id)
    return render(request, "movie_details.html", {"movie": movie})

@login_required
def delete_movie(request, movie_id):
    movie=get_object_or_404(Movie, id=movie_id)
    movie.delete()
    return redirect("homepage")
    