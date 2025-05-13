import joblib
model = joblib.load("xgb_model.pkl")
scaler = joblib.load("scaler.pkl")

def predict_game(features):
    X = scaler.transform([features])
    pred = model.predict(X)[0]
    conf = model.predict_proba(X)[0][pred]
    return pred, conf
