from uchisquashsite.models import Match
from uchisquashsite.models import db
from pandas import DataFrame
from requests import get

USSQUASH_SCHEDULE_URL = 'https://api.ussquash.com/resources/teams/29927/schedule'

MATCH_COLS = ['matchdate', 'hteamid', 'vteamid', 'Home_Matches_Won', 'Visitor_Matches_Won', 'wTeamName', 'oTeamName']

def opposing_team(row):
    return row['oTeamName'] if row['hteamid'] == 29927 else row['wTeamName']

def opposing_score(row):
    return row['Visitor_Matches_Won'] if row['hteamid'] == 29927 else row['Home_Matches_Won']

def home(row):
    return row['hteamid'] == 29927

def process_df(df):
    oteam = df.apply(opposing_team, axis=1)
    oscore = df.apply(opposing_score, axis=1)
    df['home'] = df.apply(home, axis=1)
    newdf = DataFrame({'date': df['matchdate'], 'opp': oteam, 'oscore': oscore, 'home': df['home']})
    newdf['ourscore'] = 9 - newdf['oscore']
    print(newdf)
    return newdf

def get_all_matches():
    r = get(USSQUASH_SCHEDULE_URL)
    matches = r.json()
    matches_df = DataFrame(matches)
    return process_df(matches_df[MATCH_COLS])