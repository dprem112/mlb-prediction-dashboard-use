import streamlit as st
import pandas as pd
from predictor import predict_game

st.set_page_config(page_title="MLB Prediction Dashboard", layout="centered")
st.title("⚾ MLB Prediction Dashboard")
st.markdown("Real predictions powered by machine learning.")

# Realistic example features
games = [
    {"Matchup": "Yankees vs Red Sox", "features": [3, -1.2, 5, -2, 0.8]},
    {"Matchup": "Dodgers vs Padres", "features": [1, -0.7, 3, 0, 0.4]},
    {"Matchup": "Cubs vs Brewers", "features": [-2, 0.5, -1, 2, -0.3]}
]

results = []
for game in games:
    pred, conf = predict_game(game["features"])
    results.append({
        "Matchup": game["Matchup"],
        "Predicted Winner": "Home" if pred == 1 else "Away",
        "Confidence": f"{conf:.2%}"
    })

df = pd.DataFrame(results)
st.subheader("Today's MLB Predictions")
st.table(df)
