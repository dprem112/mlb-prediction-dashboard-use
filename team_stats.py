import requests
from datetime import datetime, timedelta

def get_team_id_by_name(team_name):
    # Gets all teams and finds the matching ID
    r = requests.get("https://statsapi.mlb.com/api/v1/teams?sportId=1")
    teams = r.json().get("teams", [])
    for team in teams:
        if team["name"].lower() == team_name.lower():
            return team["id"]
    return None

def get_team_rolling_stats(team_name, window=5):
    team_id = get_team_id_by_name(team_name)
    if not team_id:
        return {
            "hits": 7.0,
            "era": 4.00,
            "strikeouts_pitch": 8.0,
            "strikeouts_bat": 8.0,
            "innings": 8.0
        }

    end_date = datetime.now()
    start_date = end_date - timedelta(days=14)
    schedule_url = f"https://statsapi.mlb.com/api/v1/schedule?teamId={team_id}&startDate={start_date.date()}&endDate={end_date.date()}&sportId=1"

    r = requests.get(schedule_url)
    games = r.json().get("dates", [])
    game_ids = [g["games"][0]["gamePk"] for g in games[:window] if g.get("games")]

    total_hits = total_er = total_ip = total_ks_pitch = total_ks_bat = count = 0

    for game_pk in game_ids:
        box_url = f"https://statsapi.mlb.com/api/v1/game/{game_pk}/boxscore"
        br = requests.get(box_url).json()

        for team_type in ["home", "away"]:
            team_data = br["teams"][team_type]
            if team_data["team"]["id"] == team_id:
                stats = team_data["teamStats"]["batting"]
                pitching = team_data["teamStats"]["pitching"]
                hits = stats.get("hits", 0)
                ks_bat = stats.get("strikeOuts", 0)
                era = pitching.get("era", 4.00)
                innings = pitching.get("inningsPitched", "0.0")
                try:
                    ip = float(innings)
                except:
                    ip = 0
                ks_pitch = pitching.get("strikeOuts", 0)

                total_hits += hits
                total_er += era
                total_ip += ip
                total_ks_pitch += ks_pitch
                total_ks_bat += ks_bat
                count += 1
                break

    if count == 0:
        return {
            "hits": 7.0,
            "era": 4.00,
            "strikeouts_pitch": 8.0,
            "strikeouts_bat": 8.0,
            "innings": 8.0
        }

    return {
        "hits": round(total_hits / count, 2),
        "era": round(total_er / count, 2),
        "strikeouts_pitch": round(total_ks_pitch / count, 2),
        "strikeouts_bat": round(total_ks_bat / count, 2),
        "innings": round(total_ip / count, 2)
    }
