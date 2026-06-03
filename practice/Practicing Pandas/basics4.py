import pandas as pd

stands = pd.read_csv("jojostandstatsv2.csv", encoding="latin1")

stands["total score"] = 0

scores = {"None": 0, "E": 1, "D": 2, "C": 3, "B": 4, "A": 5, "Infi": 7}

stat_cols = ["DEV", "PER", "PRC", "PWR", "RNG", "SPD"]

stands["total score"] = (
    stands[stat_cols].replace(scores).fillna(0).astype(int).sum(axis=1)
)


stands.sort_values("total score", ascending=False).head(10).to_csv(
    "top10.csv", index=False
)

stands.sort_values("total score").head(10).to_csv("bottom10.csv", index=False)

top = pd.read_csv("top10.csv")
bottom = pd.read_csv("bottom10.csv")
print(bottom)
print(top)
