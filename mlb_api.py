import requests
from datetime import date

def get_today_matchups():
    today = date.today().isoformat()
    url = f"https://statsapi.mlb.com/api/v1/schedule?sportId=1&date={today}"
    r = requests.get(url)
    data = r.json()

    matchups = []
    for d in data.get("dates", []):
        for game in d.get("games", []):
            matchup = {
                "gamePk": game["gamePk"],
                "home": game["teams"]["home"]["team"]["name"],
                "away": game["teams"]["away"]["team"]["name"]
            }
            matchups.append(matchup)

    return matchups
