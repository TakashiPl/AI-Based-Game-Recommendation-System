from data import DATA
import heapq


#Function to classify users age into one of available age groups
def classify_age(age):
    if age < 13:
        return "kid"
    elif age < 18:
        return "teen"
    return "adult"

#Function to get recommendations using point-based system
def get_recommendations(age, interest, debug=False):
    group = classify_age(age)
    interests = [i.lower().strip() for i in interest.split(",")]
    recommendations = []

    #For debug, to see if it works
    if debug:
        print("DEBUG age group:", group)
        print("DEBUG interests:", interests)
    

    for d in DATA:
        obiekt = {"name": d["name"], "points" : 0}
        if d["category"] in interests:
                    obiekt["points"] += 3
        if d["age_group"] == group:
                    obiekt["points"] += 2
        if obiekt["points"] > 0:
            recommendations.append(obiekt)

    #Returns three recommendations with most points
    return heapq.nlargest(3, recommendations, key=lambda x: x['points'])