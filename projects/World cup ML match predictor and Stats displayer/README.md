# Worldcup Football Match predictor and stats displayer

#### Video Demo: https://youtu.be/sEtfwtMR1K0

## Description

My project is a World Cup Match Outcome Predictor built in Python. It uses historical FIFA World Cup match data from 1930 to 2022 to calculate team statistics and predict the result of a custom match between two teams.

The program uses pandas to process the dataset and scikit-learn to train a logistic regression model. It can also show individual nation's or head to head stats of two team.

## How the Project Works

The project begins by loading a CSV file containing past World Cup matches. It then calculates statistics for each team, including:

* Win rate
* Average goals scored
* Average goals conceded
* Goal difference

These statistics are added as new features to the dataset and are used to train the machine learning model.

The model predicts whether:

* The first team wins
* The second team wins
* The match ends in a draw

## Program Features

The program includes a menu that allows the user to choose from several options.

The user can:

* Predict the winner of a custom match
* List all available teams
* View detailed statistics for a specific team
* See head-to-head history between two teams
* View the model’s accuracy
* Read an explanation of how the system works

The team statistics feature shows a team’s appearances, goals scored, goals conceded, wins, losses, draws, and previous World Cup matches.

The head-to-head feature shows past World Cup meetings between two selected teams.

## Project Files

The main file of the project is `project.py`.

This file contains:

* The main function
* Data processing functions
* Machine learning training and prediction functions
* Menu logic
* Team statistics logic
* Head-to-head comparison logic

The file `test_project.py` contains tests for important functions in the project, including the creation of result labels, goal difference columns, and the training/testing split.

## Why I Chose This Project

I chose this project because I wanted to combine my interest in football with what I have been learning in Python.

Building this project helped me learn how to work with real datasets, create useful features from raw data, train a machine learning model and evaluate its performance.

## Limitations

One limitation of the project is that it does not predict exact scores. It only predicts the match outcome: team one win, team two win, or draw.

The model is also based only on historical World Cup data, so it does not consider current team form, player injuries, squad strength.
