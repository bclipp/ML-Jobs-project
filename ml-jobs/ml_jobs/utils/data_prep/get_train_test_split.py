"""
fill me in
"""
import pandas as pd
from sklearn.model_selection import train_test_split


def get_train_test_split(sales):
    """
    fill me in
    """
    pd_sales = pd.DataFrame(sales)
    y = pd_sales["AVG"]
    X = pd_sales.drop("AVG", axis=1)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.34, random_state=613
    )
    return {"X_train": X_train, "X_test": X_test, "y_train": y_train, "y_test": y_test}
