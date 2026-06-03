import pandas as pd

world = pd.read_csv('World_Cup_All_Match_Dataset.csv', encoding="latin1")

rows, col = world.shape

print(f'number of matches are {rows}\n')

print(f'first ten rows are {world.head(10)}\n')

for col in world.columns:
    print(col)
