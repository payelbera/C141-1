import numpy as np
import pandas as pd

df = pd.read_csv("final.csv")
c = df["vote_average"].mean()
m = df["vote_count"].quantile(0.9)
q_movies = df.copy().loc[df["vote_count"]>=m]

def weighted_rating(x, m=m, C=c):
    v = x["vote_count"]
    r = x["vote_average"]
    return (v/(v+m)*r)+(m/(m+v)*C)

q_movies["score"] = q_movies.apply(weighted_rating, axis=1)
q_movies = q_movies.sort_values("score", ascending=False)
output = q_movies[["title_x", "poster_link", "release_data", "runtime", "vote_average", "overview"]].head(20).values.tolist()
