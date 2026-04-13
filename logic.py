import json
import heapq

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

#Function to get recommendations using point-based system
def get_recommendations(age, interest, debug=False):
    DATA = load_data()
    group = classify_age(age)
    tags = [i.lower().strip() for i in interest.split(",")]
    tags_set = set(tags)
    recommendations = []

    #For debug, to see if it works
    if debug:
        print("DEBUG age group:", group)
        print("DEBUG interests:", tags)
    

    for d in DATA:
        obiekt = {"name": d["name"], "points" : 0}
        game_tags = set(d["tags"])
        common_tags = tags_set & game_tags
        obiekt["points"] += len(common_tags)
        if d["age_group"] == group:
                    obiekt["points"] += 2
        if obiekt["points"] > 0:
            recommendations.append(obiekt)

    #Returns three recommendations with most points
    return heapq.nlargest(3, recommendations, key=lambda x: x['points'])