import pandas as pd

world = pd.read_csv("World_Cup_All_Match_Dataset.csv", encoding="latin1")

each_team_home = world.groupby("Home_Team_Name", as_index=False)[
    "Home_Team_Score"
].sum()

each_team_away = world.groupby("Away_Team_Name", as_index=False)[
    "Away_Team_Score"
].sum()

each_team_home = each_team_home.rename(
    columns={"Home_Team_Name": "Team", "Home_Team_Score": "Score"}
)

each_team_away = each_team_away.rename(
    columns={"Away_Team_Name": "Team", "Away_Team_Score": "Score"}
)


merged_split = pd.merge(each_team_home, each_team_away, on="Team")

merged_split["total score"] = merged_split["Score_x"] + merged_split["Score_y"]

merged_split.drop(columns=["Score_x", "Score_y"], inplace=True)


print(merged_split.sort_values("total score", ascending=False).head(5))
