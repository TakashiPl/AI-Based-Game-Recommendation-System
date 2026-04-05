from data import DATA

def classify_age(age):
    if age < 13:
        return "kid"
    elif age < 18:
        return "teen"
    return "adult"

def validate_interests(interests):
    from data import DATA
    return [i for i in interests if i in DATA]

def get_recommendations(age, interest, debug=False):
    group = classify_age(age)
    interests = [i.lower().strip() for i in interest.split(",")]
    interests = validate_interests(interests)
    recommendations = []

    if debug:
        print("DEBUG age group:", group)
        print("DEBUG interests:", interests)
        print("DEBUG data keys:", DATA.keys())
    

    for i in interests:
        for key in DATA:
            if key in i:
                if debug:
                    print("Matched:", i, "->", key)
                recommendations.extend(DATA[key][group])

    return recommendations