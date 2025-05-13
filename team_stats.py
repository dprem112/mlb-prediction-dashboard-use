import requests
import random

# Simulated function to mimic team rolling stats from MLB API
def get_team_rolling_stats(team_name):
    # NOTE: This would normally pull and average the last 3–5 games from an API
    # For now, return randomized but realistic stat ranges
    return {
        "hits": round(random.uniform(6.5, 10.0), 2),
        "era": round(random.uniform(2.5, 5.0), 2),
        "strikeouts_pitch": round(random.uniform(7.5, 10.5), 2),
        "strikeouts_bat": round(random.uniform(6.0, 10.0), 2),
        "innings": round(random.uniform(7.0, 9.0), 2)
    }
