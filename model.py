import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression


def modeldump():
    df = pd.read_csv("SBP.csv")

    x = df[["Age", "Weight"]]
    y = df["SBP"]

    LR = LinearRegression()
    LR.fit(x, y)

    joblib.dump(LR, "LR.pkl")





modeldump()
