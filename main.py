from utils import get_non_empty_string, get_number
from logic import get_recommendations

def main():
    age = get_number("Enter your age: ", int, 0, 120)
    interest = get_non_empty_string(
        "Enter your interests (comma separated, e.g. games, music): "
        )

    recommendations = get_recommendations(age, interest)

    print("\n--- RESULT ---")
    if recommendations:
        print("We recommend:", ", ".join(recommendations))
    else:
        print("No recommendations found. Try: games, music")

if __name__ == "__main__":
    main()