import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
import sys
from tabulate import tabulate

df = pd.read_csv("World_Cup_All_Match_Dataset.csv", encoding="latin-1")

team_list = [
    "France",
    "United States",
    "Yugoslavia",
    "Romania",
    "Argentina",
    "Chile",
    "Uruguay",
    "Brazil",
    "Paraguay",
    "Austria",
    "Czechoslovakia",
    "Germany",
    "Hungary",
    "Italy",
    "Spain",
    "Sweden",
    "Switzerland",
    "Cuba",
    "England",
    "West Germany",
    "Turkey",
    "Northern Ireland",
    "Soviet Union",
    "Mexico",
    "Wales",
    "Portugal",
    "North Korea",
    "Peru",
    "Belgium",
    "Bulgaria",
    "East Germany",
    "Zaire",
    "Poland",
    "Australia",
    "Scotland",
    "Netherlands",
    "Haiti",
    "Tunisia",
    "Algeria",
    "Honduras",
    "Canada",
    "Morocco",
    "South Korea",
    "Iraq",
    "Denmark",
    "United Arab Emirates",
    "Costa Rica",
    "Cameroon",
    "Republic of Ireland",
    "Colombia",
    "Norway",
    "Nigeria",
    "Saudi Arabia",
    "Bolivia",
    "Russia",
    "Greece",
    "Jamaica",
    "South Africa",
    "Japan",
    "Croatia",
    "China",
    "Senegal",
    "Slovenia",
    "Ecuador",
    "Trinidad and Tobago",
    "Serbia and Montenegro",
    "Angola",
    "Czech Republic",
    "Togo",
    "Iran",
    "Ivory Coast",
    "Ghana",
    "Ukraine",
    "Serbia",
    "New Zealand",
    "Slovakia",
    "Bosnia and Herzegovina",
    "Egypt",
    "Iceland",
    "Panama",
    "Qatar",
    "Dutch East Indies",
    "Israel",
    "El Salvador",
    "Kuwait",
]
wins_rate_dict = {
    "France": 0,
    "United States": 0,
    "Yugoslavia": 0,
    "Romania": 0,
    "Argentina": 0,
    "Chile": 0,
    "Uruguay": 0,
    "Brazil": 0,
    "Paraguay": 0,
    "Austria": 0,
    "Czechoslovakia": 0,
    "Germany": 0,
    "Hungary": 0,
    "Italy": 0,
    "Spain": 0,
    "Sweden": 0,
    "Switzerland": 0,
    "Cuba": 0,
    "England": 0,
    "West Germany": 0,
    "Turkey": 0,
    "Northern Ireland": 0,
    "Soviet Union": 0,
    "Mexico": 0,
    "Wales": 0,
    "Portugal": 0,
    "North Korea": 0,
    "Peru": 0,
    "Belgium": 0,
    "Bulgaria": 0,
    "East Germany": 0,
    "Zaire": 0,
    "Poland": 0,
    "Australia": 0,
    "Scotland": 0,
    "Netherlands": 0,
    "Haiti": 0,
    "Tunisia": 0,
    "Algeria": 0,
    "Honduras": 0,
    "Canada": 0,
    "Morocco": 0,
    "South Korea": 0,
    "Iraq": 0,
    "Denmark": 0,
    "United Arab Emirates": 0,
    "Costa Rica": 0,
    "Cameroon": 0,
    "Republic of Ireland": 0,
    "Colombia": 0,
    "Norway": 0,
    "Nigeria": 0,
    "Saudi Arabia": 0,
    "Bolivia": 0,
    "Russia": 0,
    "Greece": 0,
    "Jamaica": 0,
    "South Africa": 0,
    "Japan": 0,
    "Croatia": 0,
    "China": 0,
    "Senegal": 0,
    "Slovenia": 0,
    "Ecuador": 0,
    "Trinidad and Tobago": 0,
    "Serbia and Montenegro": 0,
    "Angola": 0,
    "Czech Republic": 0,
    "Togo": 0,
    "Iran": 0,
    "Ivory Coast": 0,
    "Ghana": 0,
    "Ukraine": 0,
    "Serbia": 0,
    "New Zealand": 0,
    "Slovakia": 0,
    "Bosnia and Herzegovina": 0,
    "Egypt": 0,
    "Iceland": 0,
    "Panama": 0,
    "Qatar": 0,
    "Dutch East Indies": 0,
    "Israel": 0,
    "El Salvador": 0,
    "Kuwait": 0,
}
avg_goals_scored_dict = {
    "France": 0,
    "United States": 0,
    "Yugoslavia": 0,
    "Romania": 0,
    "Argentina": 0,
    "Chile": 0,
    "Uruguay": 0,
    "Brazil": 0,
    "Paraguay": 0,
    "Austria": 0,
    "Czechoslovakia": 0,
    "Germany": 0,
    "Hungary": 0,
    "Italy": 0,
    "Spain": 0,
    "Sweden": 0,
    "Switzerland": 0,
    "Cuba": 0,
    "England": 0,
    "West Germany": 0,
    "Turkey": 0,
    "Northern Ireland": 0,
    "Soviet Union": 0,
    "Mexico": 0,
    "Wales": 0,
    "Portugal": 0,
    "North Korea": 0,
    "Peru": 0,
    "Belgium": 0,
    "Bulgaria": 0,
    "East Germany": 0,
    "Zaire": 0,
    "Poland": 0,
    "Australia": 0,
    "Scotland": 0,
    "Netherlands": 0,
    "Haiti": 0,
    "Tunisia": 0,
    "Algeria": 0,
    "Honduras": 0,
    "Canada": 0,
    "Morocco": 0,
    "South Korea": 0,
    "Iraq": 0,
    "Denmark": 0,
    "United Arab Emirates": 0,
    "Costa Rica": 0,
    "Cameroon": 0,
    "Republic of Ireland": 0,
    "Colombia": 0,
    "Norway": 0,
    "Nigeria": 0,
    "Saudi Arabia": 0,
    "Bolivia": 0,
    "Russia": 0,
    "Greece": 0,
    "Jamaica": 0,
    "South Africa": 0,
    "Japan": 0,
    "Croatia": 0,
    "China": 0,
    "Senegal": 0,
    "Slovenia": 0,
    "Ecuador": 0,
    "Trinidad and Tobago": 0,
    "Serbia and Montenegro": 0,
    "Angola": 0,
    "Czech Republic": 0,
    "Togo": 0,
    "Iran": 0,
    "Ivory Coast": 0,
    "Ghana": 0,
    "Ukraine": 0,
    "Serbia": 0,
    "New Zealand": 0,
    "Slovakia": 0,
    "Bosnia and Herzegovina": 0,
    "Egypt": 0,
    "Iceland": 0,
    "Panama": 0,
    "Qatar": 0,
    "Dutch East Indies": 0,
    "Israel": 0,
    "El Salvador": 0,
    "Kuwait": 0,
}
avg_goals_conceded_dict = {
    "France": 0,
    "United States": 0,
    "Yugoslavia": 0,
    "Romania": 0,
    "Argentina": 0,
    "Chile": 0,
    "Uruguay": 0,
    "Brazil": 0,
    "Paraguay": 0,
    "Austria": 0,
    "Czechoslovakia": 0,
    "Germany": 0,
    "Hungary": 0,
    "Italy": 0,
    "Spain": 0,
    "Sweden": 0,
    "Switzerland": 0,
    "Cuba": 0,
    "England": 0,
    "West Germany": 0,
    "Turkey": 0,
    "Northern Ireland": 0,
    "Soviet Union": 0,
    "Mexico": 0,
    "Wales": 0,
    "Portugal": 0,
    "North Korea": 0,
    "Peru": 0,
    "Belgium": 0,
    "Bulgaria": 0,
    "East Germany": 0,
    "Zaire": 0,
    "Poland": 0,
    "Australia": 0,
    "Scotland": 0,
    "Netherlands": 0,
    "Haiti": 0,
    "Tunisia": 0,
    "Algeria": 0,
    "Honduras": 0,
    "Canada": 0,
    "Morocco": 0,
    "South Korea": 0,
    "Iraq": 0,
    "Denmark": 0,
    "United Arab Emirates": 0,
    "Costa Rica": 0,
    "Cameroon": 0,
    "Republic of Ireland": 0,
    "Colombia": 0,
    "Norway": 0,
    "Nigeria": 0,
    "Saudi Arabia": 0,
    "Bolivia": 0,
    "Russia": 0,
    "Greece": 0,
    "Jamaica": 0,
    "South Africa": 0,
    "Japan": 0,
    "Croatia": 0,
    "China": 0,
    "Senegal": 0,
    "Slovenia": 0,
    "Ecuador": 0,
    "Trinidad and Tobago": 0,
    "Serbia and Montenegro": 0,
    "Angola": 0,
    "Czech Republic": 0,
    "Togo": 0,
    "Iran": 0,
    "Ivory Coast": 0,
    "Ghana": 0,
    "Ukraine": 0,
    "Serbia": 0,
    "New Zealand": 0,
    "Slovakia": 0,
    "Bosnia and Herzegovina": 0,
    "Egypt": 0,
    "Iceland": 0,
    "Panama": 0,
    "Qatar": 0,
    "Dutch East Indies": 0,
    "Israel": 0,
    "El Salvador": 0,
    "Kuwait": 0,
}
results_dict = {
    "home team win": "team1_win",
    "away team win": "team2_win",
    "draw": "draw",
}


def main():
    calc_win_rate()
    calc_avg_goals_scored()
    win_rate_diff()
    calc_avg_goals_conceded()
    goal_diff()
    results_label()
    df.to_csv("Worldcup dataset (new columns).csv")
    world = pd.read_csv("Worldcup dataset (new columns).csv", encoding="latin-1")
    X_train, X_test, y_train, y_test = train_test_x_y(world)
    predictions, y_test, X_test, ml_alg = predict(X_train, X_test, y_train, y_test)

    try:
        decision = int(
            input(
                "What do you want the model to do? \n1. Predict winner of a custom match\n2. List all available teams\n3. Output a teams stats\n4. Show Head to Head stats between two teams \n5. Explain how the system works\n6. Show the systems accuracy %. \nChoice: "
            )
        )
        if decision == 1:
            custom_match(ml_alg)
        elif decision == 2:
            for country in team_list:
                print(country)
        elif decision == 3:
            stats(df)
        elif decision == 4:
            head_to_head(df)
        elif decision == 6:
            evaluate(predictions, y_test, X_test)
        elif decision == 5:
            print(
                "This model uses historical World Cup data of each match from 1930 to 2022.\n"
            )
            print(
                "It calculates each team's win rate, average goals scored, average goals conceded, and goal difference.\n"
            )
            print(
                "A logistic regression model then predicts whether team1 wins, team2 wins, or the match is a draw. The model is not perfect and struggles most with predicting draws."
            )
    except ValueError:
        sys.exit("Please enter only numbers 1 through 6")
    except TypeError:
        sys.exit("Please enter only numbers 1 through 6")


def calc_win_rate():

    for country in team_list:
        home_wins = df.loc[
            (df["Home Team Name"] == country) & (df["Result"] == "home team win")
        ]
        home_appearances = df.loc[(df["Home Team Name"] == country)]
        away_wins = df.loc[
            (df["Away Team Name"] == country) & (df["Result"] == "away team win")
        ]
        away_appearances = df.loc[(df["Away Team Name"] == country)]
        if len(home_appearances) + len(away_appearances) != 0:
            wins_rate_dict.update(
                {
                    country: (len(home_wins) + len(away_wins))
                    / (len(home_appearances) + len(away_appearances))
                }
            )

    df["Home team win rate"] = df["Home Team Name"].map(wins_rate_dict)
    df["Away team win rate"] = df["Away Team Name"].map(wins_rate_dict)


def calc_avg_goals_scored():
    for country in team_list:
        number_home_appearances = len(df.loc[(df["Home Team Name"] == country)])
        score_home = df.loc[df["Home Team Name"] == country, "Home Team Score"]
        number_away_appearances = len(df.loc[(df["Away Team Name"] == country)])
        score_away = df.loc[df["Away Team Name"] == country, "Away Team Score"]
        total = score_home.sum() + score_away.sum()
        total_apps = number_home_appearances + number_away_appearances
        if total_apps > 0:
            avg_goals_scored_dict.update({country: total / total_apps})

    df["Home team avg goals scored"] = df["Home Team Name"].map(avg_goals_scored_dict)
    df["Away team avg goals scored"] = df["Away Team Name"].map(avg_goals_scored_dict)


def win_rate_diff():
    df["win rate difference"] = df["Home team win rate"] - df["Away team win rate"]


def calc_avg_goals_conceded():
    for country in team_list:
        number_home_appearances = len(df.loc[(df["Home Team Name"] == country)])
        score_home_conceded = df.loc[df["Home Team Name"] == country, "Away Team Score"]
        number_away_appearances = len(df.loc[(df["Away Team Name"] == country)])
        score_away_conceded = df.loc[df["Away Team Name"] == country, "Home Team Score"]
        total = score_home_conceded.sum() + score_away_conceded.sum()
        total_apps = number_home_appearances + number_away_appearances
        if total_apps > 0:
            avg_goals_conceded_dict.update({country: total / total_apps})

    df["Home team avg goals conceded"] = df["Home Team Name"].map(
        avg_goals_conceded_dict
    )
    df["Away team avg goals conceded"] = df["Away Team Name"].map(
        avg_goals_conceded_dict
    )


def goal_diff():
    df["home goal difference"] = (
        df["Home team avg goals scored"] - df["Home team avg goals conceded"]
    )
    df["away goal difference"] = (
        df["Away team avg goals scored"] - df["Away team avg goals conceded"]
    )
    df["goal difference difference"] = (
        df["home goal difference"] - df["away goal difference"]
    )


def results_label():
    df["result_label"] = df["Result"].map(results_dict)


def train_test_x_y(world):
    X = world[
        [
            "Home team win rate",
            "Away team win rate",
            "Home team avg goals scored",
            "Away team avg goals scored",
            "win rate difference",
            "Home team avg goals conceded",
            "Away team avg goals conceded",
            "home goal difference",
            "away goal difference",
            "goal difference difference",
        ]
    ]
    y = world["result_label"]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, random_state=67, test_size=0.3
    )
    return X_train, X_test, y_train, y_test


def predict(X_train, X_test, y_train, y_test):
    ml_alg = LogisticRegression().fit(X_train, y_train)
    predictions = ml_alg.predict(X_test)

    return predictions, y_test, X_test, ml_alg


"""
def evaluate(predictions, y_test, X_test):
    print(f'{(accuracy_score(y_test, predictions))*100:.2f}')
    print(classification_report(y_test, predictions))
"""


def custom_match(ml_alg):
    team1 = input("enter the first team: ").title().strip()
    team2 = input("enter the second team: ").title().strip()
    try:
        stats = {
            "Home team win rate": wins_rate_dict.get(team1),
            "Away team win rate": wins_rate_dict.get(team2),
            "Home team avg goals scored": avg_goals_scored_dict.get(team1),
            "Away team avg goals scored": avg_goals_conceded_dict.get(team2),
            "win rate difference": (
                wins_rate_dict.get(team1) - wins_rate_dict.get(team2)
            ),
            "Home team avg goals conceded": avg_goals_conceded_dict.get(team1),
            "Away team avg goals conceded": avg_goals_conceded_dict.get(team2),
            "home goal difference": avg_goals_scored_dict.get(team1)
            - avg_goals_conceded_dict.get(team1),
            "away goal difference": avg_goals_scored_dict.get(team2)
            - avg_goals_conceded_dict.get(team2),
            "goal difference difference": (
                avg_goals_scored_dict.get(team1) - avg_goals_conceded_dict.get(team1)
            )
            - (avg_goals_scored_dict.get(team2) - avg_goals_conceded_dict.get(team2)),
        }
        custom_match_df = pd.DataFrame([stats])
        result = str(ml_alg.predict(custom_match_df))
        print(f"\nso its {team1} Vs {team2}")
        print(f"and the model predicts......\n")

        if result[6] == "2":
            print(f"{team2} to beat {team1}")
        else:
            print(f"{team1} to beat {team2}")

    except TypeError:
        print("Country not found")


def evaluate(predictions, y_test, X_test):
    print(
        f"The Accuracy of this system is {(accuracy_score(y_test, predictions))*100:.2f}%"
    )


def stats(df):
    country = (
        input("enter the country whose stats you would like to see: ").title().strip()
    )
    print("")
    all_appearances_df = df.query(
        "`Home Team Name` == @country or `Away Team Name` == @country"
    )[
        [
            "tournament Name",
            "Match Name",
            "Stage Name",
            "Home Team Name",
            "Away Team Name",
            "Home Team Score",
            "Away Team Score",
            "Result",
        ]
    ]
    if all_appearances_df.empty:
        print("Country not found")
        return
    appearances = len(all_appearances_df)

    home_score = all_appearances_df.query("`Home Team Name` == @country")[
        "Home Team Score"
    ].sum()
    away_score = all_appearances_df.query("`Away Team Name` == @country")[
        "Away Team Score"
    ].sum()
    scored = home_score + away_score

    home_wins = all_appearances_df.query(
        "`Home Team Name` == @country and Result == 'home team win'"
    )
    away_wins = all_appearances_df.query(
        "`Away Team Name` == @country and Result == 'away team win'"
    )
    wins = len(home_wins) + len(away_wins)

    home_losses = all_appearances_df.query(
        "`Home Team Name` == @country and Result == 'away team win'"
    )
    away_losses = all_appearances_df.query(
        "`Away Team Name` == @country and Result == 'home team win'"
    )
    losses = len(home_losses) + len(away_losses)

    home_draws = all_appearances_df.query(
        "`Home Team Name` == @country and Result == 'draw'"
    )
    away_draws = all_appearances_df.query(
        "`Away Team Name` == @country and Result == 'draw'"
    )
    draws = len(home_draws) + len(away_draws)

    home_conceded = all_appearances_df.query("`Home Team Name` == @country")[
        "Away Team Score"
    ].sum()
    away_conceded = all_appearances_df.query("`Away Team Name` == @country")[
        "Home Team Score"
    ].sum()
    conceded = home_conceded + away_conceded

    try:
        print(f"{country} has {appearances} appearances in the world cup")
        if scored == 1:
            print(f"{country} has scored {scored} goal")
        else:
            print(f"{country} has scored {scored} goals")
        if conceded == 1:
            print(f"{country} has conceded {conceded} goal")
        else:
            print(f"{country} has conceded {conceded} goals")
        if wins == 1:
            print(f"{country} has {wins} win")
        else:
            print(f"{country} has {wins} wins")
        if losses == 1:
            print(f"{country} has {losses} loss")
        else:
            print(f"{country} has {losses} losses")
        if draws == 1:
            print(f"{country} has {draws} draw")
        else:
            print(f"{country} has {draws} draws")

        print(f"win rate of {country} is {wins_rate_dict.get(country):.2f}")
        print(
            f"Averge goals scored of {country} is {avg_goals_scored_dict.get(country):.2f}"
        )
        print(
            f"Averge goals conceded of {country} is {avg_goals_conceded_dict.get(country):.2f}"
        )
        print("")
        print(f"here are all appearances of {country}:")
        print("")
        print("")
        print(
            tabulate(
                all_appearances_df,
                headers="keys",
                tablefmt="psql",
                showindex=False,
            )
        )

    except ValueError:
        print("Country not found")


def head_to_head(df):
    print("")
    team1 = input("enter the first team: ").title().strip()
    team2 = input("enter the second team: ").title().strip()
    team1_wins = 0
    team2_wins = 0
    draw = 0

    all_matches = df.query(
        "(`Home Team Name` == @team1 and `Away Team Name` == @team2) or "
        "(`Home Team Name` == @team2 and `Away Team Name` == @team1)"
    )[
        [
            "tournament Name",
            "Match Name",
            "Stage Name",
            "Stadium Name",
            "Result",
            "Home Team Name",
            "Away Team Name",
            "Home Team Score",
            "Away Team Score",
        ]
    ]

    temp_df = all_matches.query(
        "(`Home Team Name` == @team1 and Result == 'home team win') or (`Away Team Name` == @team1 and Result == 'away team win')"
    )
    team1_wins = len(temp_df)
    temp_df2 = all_matches.query(
        "(`Home Team Name` == @team2 and Result == 'home team win') or (`Away Team Name` == @team2 and Result == 'away team win')"
    )
    team2_wins = len(temp_df2)
    drawdf = all_matches.query("Result == 'draw'")
    draw = len(drawdf)
    team1_home_score = all_matches.query("(`Home Team Name` == @team1)")[
        "Home Team Score"
    ].sum()
    team1_away_score = all_matches.query("(`Away Team Name` == @team1)")[
        "Away Team Score"
    ].sum()
    team1_score = team1_home_score + team1_away_score
    team2_home_score = all_matches.query("(`Home Team Name` == @team2)")[
        "Home Team Score"
    ].sum()
    team2_away_score = all_matches.query("(`Away Team Name` == @team2)")[
        "Away Team Score"
    ].sum()
    team2_score = team2_home_score + team2_away_score

    if all_matches.empty:
        print(
            f"{team1} and {team2} have never played against each other in the World cup"
        )
    else:
        print("")
        print(
            tabulate(
                all_matches[
                    [
                        "tournament Name",
                        "Match Name",
                        "Stage Name",
                        "Stadium Name",
                        "Result",
                    ]
                ],
                headers="keys",
                tablefmt="psql",
                showindex=False,
            )
        )
        print("")
        if (team1_score > 1) and (team2_score > 1):
            print(
                f"{team1} wins: {team1_wins}\n{team2} wins: {team2_wins}\nDraws: {draw}\n{team1} has scored {team1_score} goals\n{team2} has scored {team2_score} goals"
            )
        elif team1_score <= 1:
            print(
                f"{team1} wins: {team1_wins}\n{team2} wins: {team2_wins}\nDraws: {draw}\n{team1} has scored {team1_score} goal\n{team2} has scored {team2_score} goals"
            )
        elif team2_score <= 1:
            print(
                f"{team1} wins: {team1_wins}\n{team2} wins: {team2_wins}\nDraws: {draw}\n{team1} has scored {team1_score} goals\n{team2} has scored {team2_score} goal"
            )


if __name__ == "__main__":
    main()
