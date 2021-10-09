from flask import Flask, app, jsonify, request
import csv

all_movies = []
with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]

like_movies = []
unlike_movies = []
unwatch_movies = []
app = Flask(__name__)
@app.route("/get-movies")
def get_movie():
    return jsonify({
        "data": all_movies[0],
        "status": "success"
    })

@app.route("/liked-movies", methods=["POST"])
def liked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    like_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unliked-movies", methods=["POST"])
def unliked_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unlike_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

@app.route("/unwatched-movies", methods=["POST"])
def unwatched_movie():
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unwatch_movies.append(movie)
    return jsonify({
        "status": "success"
    }), 201

if __name__ == "__main__":
    app.run()