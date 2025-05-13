# In a real system, this would call the MLB API or a stat provider
# For now, we return dummy but structured values for each team

def get_team_rolling_stats(team_name):
    dummy_stats = {
        "hits": 8.2,
        "era": 3.75,
        "strikeouts_pitch": 9.1,
        "strikeouts_bat": 8.4,
        "innings": 8.0
    }
    return dummy_stats
