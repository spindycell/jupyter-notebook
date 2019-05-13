import pandas as pd
import numpy as np
import csv

data = pd.read_csv("instagram_logs.csv")

# Get user
nama = "|".join(data["username"].values)
nama = nama.split("|")
names, freqs = np.unique(nama, return_counts=True)
# print(names)
print("Total Unique Username dicari :",len(names))

most_pop_user = np.array([(name, freq) for freq, name in sorted(zip(freqs, names), reverse=True)])[:5]
print("Top 5 user dicari: ", most_pop_user)

print()

# # Get uploads
uploads_list = str(data["uploads"].values)
print("Data uploads by users : ",uploads_list)
# names, freqs = np.unique(uploads_list, return_counts=True)
# print(names)
# print("Total Unique Saved uploads:",len(uploads_list))

# most_pop_director = np.array([[name, freq] for freq, name in sorted(zip(freqs, names), reverse=True)])[:5]
# print("Top 5:", most_pop_director)

# print()

# # Get Genres Features
# genre_list = "|".join(data["genres"].values)
# genre_list = genre_list.split("|")
# names, freqs = np.unique(genre_list, return_counts=True)
# print("Total Unique Saved Genres:",len(names))

# all_genres = np.array([[name, freq] for freq, name in sorted(zip(freqs, names), reverse=True)])
# print("All Genres:", all_genres)

# print()

# # Get All Features
# features = np.array([])
# features = np.concatenate([features, all_genres[:,0], most_pop_director[:,0], most_pop_actor[:,0]])
# print("Features:",features,"Length:",len(features))

