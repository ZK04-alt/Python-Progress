import pandas as pd

world = pd.read_csv("World_Cup_All_Match_Dataset.csv", encoding="latin1")

country = input("enter team name: ").capitalize()

world["year"] = world["tournament Name"].str.split(" ").str[0]

print(
    world.loc[
        world["Match Name"].str.contains(country),
        ["year", "Home Team Name", "Away Team Name", "Score"],
    ]
)
