# API_Development_IPL_Data
### Developing different API for IPL Dataset showcasing teams and team vs team and also showcasing batsman record.
To develop APIs for the IPL dataset showcasing team records, team vs team matchups, and batsman records, you'll need to structure your data and define the endpoints. Here's a step-by-step guide for each API:

1. API for Teams List
This API should return the list of all IPL teams.

- Endpoint: /teams
- Method: GET

2. API for Team vs Team Records
This API should return the head-to-head record between two teams.

- Endpoint: /team_vs_team
- Method: GET

#### - Query Parameters:

- team1: First team
- team2: Second team

3. API for Batsman Records
This API will return stats for a specific batsman.

- Endpoint: /batsman_stats
- Method: GET

#### Query Parameters:

- batsman_name: Name of the batsman
