import pandas as pd
file_path=r"C:\Users\RUSHIKESH\Desktop\Top Mentor JOB Preparation\campusx\Untitled Folder\ipl-matches.csv"
matches=pd.read_csv(file_path)
print(matches.head(2))

def teamsAPI():
    teams = list(set(list(matches['Team1']) + list(matches['Team2'])))
    team_dict={
        'teams':teams
    }
    return team_dict


def teamVteamAPI(team1,team2):

    valid_teams = list(set(list(matches['Team1']) + list(matches['Team2'])))

    if team1 in valid_teams and team2 in valid_teams:

        temp_df = matches[(matches['Team1'] == team1) & (matches['Team2'] == team2) | (matches['Team1'] == team2) & (matches['Team2'] == team1)]
        total_matches = temp_df.shape[0]

        matches_won_team1 = temp_df['WinningTeam'].value_counts()[team1]
        matches_won_team2 = temp_df['WinningTeam'].value_counts()[team2]

        draws = total_matches - (matches_won_team1 + matches_won_team2)

        response = {
              'total_matches': str(total_matches),
              team1: str(matches_won_team1),
              team2: str(matches_won_team2),
              'draws': str(draws)
          }

        return response
    else:
        return {'message':'invalid team name'}

