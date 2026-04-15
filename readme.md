# AI Recommendation System

A game recommendation system that uses Machine Learning to match titles based on user preferences and age categories.

## About the Project

This application allows user to enter their age and a list of preffered tags (e.g. open world, shooter, rpg). The system then searches the database for the best-matched games using Nautral Language Processing (NLP) techniques

## Features

- ML Engine: Uses TF-IDF vectorization and Cosine Similarity to calculate recommendation accuracy.
- Web Interface: A modern UI buil entirely with the Streamlit library
- Hybrid Logic: Combines mathematical tag similarity with age group filtering.

## Tech Stack
- Language: Python 3.x
- AI/ML Libraries: scikit-learn (TfidfVectorizer, cosine_similarity)
- Frontend: Streamlit
- Data Format: JSON

## How it works
1. Data Preparation: Game tags are cleaned and joined for analysis.
2. Vectorization: Words are converted into numerical vectors. Rare and unique tags (e.g. soulslike) are given higher weights.
3. Similarity Calculation: The system measures the mathematical "distance" between the user's input vector and the game vectors in the database.
4. Ranking: The final score is a combination of tag similarity and age-matching bonus.

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/TakashiPl/AI-Based-Game-Recommendation-System.git](https://      github.com/TakashiPl/AI-Based-Game-Recommendation-System.git)
   ```
2. **Install dependencies:**
   ```bash
   pip install scikit-learn streamlit
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Project Structure
* `app.py` - The Streamlit frontend and user interface.
* `logic.py` - The "brain" of the app containing the ML logic and data processing.
* `data.json` - The database containing game titles, tags, and age groups.
* `utils.py` - Helper functions for data validation.
