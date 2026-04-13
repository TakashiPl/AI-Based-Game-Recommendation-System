from utils import get_non_empty_string, get_number
from logic import get_recommendations

def main():
    age = get_number("Enter your age: ", int, 0, 120)
    tags = get_non_empty_string(
        "Enter tags to search for your desired game (coma seperated, e.g. battleroyale): "
    )

    recommendations = get_recommendations(age, tags)

    print("\n--- RESULT ---")
    if recommendations:
        print("We recommend: ")
        for k in recommendations: 
           print(k["name"])
    else:
        print("No recommendations found. Try: battleroyale, sandbox")

if __name__ == "__main__":
    main()