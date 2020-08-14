from flask import Flask, render_template, request
import json, os

app = Flask(__name__)

@app.route("/")
def index():
    movies = {}

    if os.path.exists("movies.json"):

        with open("movies.json") as movies_file:
            movies = json.load(movies_file)
    else:
        with open("movies.json", "w") as f:
            f.write("[]") 

        new_movie = [{
            "title": "Dummy Movies",
            "year": 2005,
            "budget": "USD 700m",
            "cast": "People", 
        }] 
        movies = new_movie

    return render_template("index.html", movies=movies)


    new_movie = [{
            "title": "Prison-Break",
            "year": 2005,
            "budget": "USD 700m",
            "cast": "People",

  }]
    movies = new_movie

    return render_template(
            "index.html", movies=movies)

@app.route("/new-movie", methods =['POST', 'GET'])
def new_movie():

    if request.method == 'GET':
        return render_template("new_movie.html")
    else:
        new_movie = {}
        new_movie['title'] = request.form['title']
        new_movie['year'] = request.form['year']
        new_movie['budget'] = request.form['budget']
        new_movie['cast'] = request.form['cast']
        
        with open("movies.json", "w") as f:
            # f.write(str(new_movie))
            json.dump(new_movie,f)

    return render_template(
            "new_movie.html",
            success = f"Movie '{new_movie['title']}' was successfully added."
        )

