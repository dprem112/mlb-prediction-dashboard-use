import streamlit as st
import pandas as pd
from mlb_api import get_today_matchups
from generate_features import build_features
from predictor import predict_game

st.set_page_config(page_title="Live MLB Predictions", layout="centered")
st.title("⚾ MLB Prediction Dashboard")

st.markdown("Below are today's MLB matchups and predicted outcomes using our trained model.")

games = get_today_matchups()

if not games:
    st.warning("No games found for today.")
else:
    predictions = []
    for game in games:
        features = build_features(game)
        pred, conf = predict_game(features)
        predictions.append({
            "Matchup": f"{game['away']} @ {game['home']}",
            "Predicted Winner": game["home"] if pred == 1 else game["away"],
            "Confidence": f"{conf:.2%}"
        })

    df = pd.DataFrame(predictions)
    st.subheader("Predictions")
    st.table(df)
