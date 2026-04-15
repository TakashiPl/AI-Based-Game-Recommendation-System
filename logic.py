from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import heapq


def prepare_tags_for_ml(data):
    return [' '.join(d["tags"]) for d in data]

#Function to load data from json file
def load_data(filepath="recommendation-ai\AI Recommendation System\data.json"):
      with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
      
#Function to classify users age into one of available age groups
def classify_age(age):
    if age < 13:
        return "kid"
    elif age < 18:
        return "teen"
    return "adult"

DATA = load_data()


#Function to get recommendations using point-based system
def get_recommendations(age, tag, debug=False):
    group = classify_age(age)
    tag_strings = prepare_tags_for_ml(DATA)
    vecotrizer = TfidfVectorizer()
    tfidf_matrix = vecotrizer.fit_transform(tag_strings)
    user_input_cleaned = tag.replace(","," ")
    user_vector = vecotrizer.transform([user_input_cleaned])
    similarity_scores = cosine_similarity(user_vector, tfidf_matrix)
    scores_list = similarity_scores.flatten()
    recommendations = []
    for index, score in enumerate(scores_list):
        tag_points = score * 10
        obiekt = {"name": DATA[index]["name"], "points": tag_points}
        if DATA[index]["age_group"] == group:
            obiekt["points"] += 2
        if obiekt["points"] > 0:
            recommendations.append(obiekt)

    #Returns three recommendations with most points using heapq library
    return heapq.nlargest(3, recommendations, key=lambda x: x['points'])