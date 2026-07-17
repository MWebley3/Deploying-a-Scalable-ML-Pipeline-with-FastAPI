import pytest
# TODO: add necessary import
import numpy as np
import pandas as pd
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier
from ml.model import compute_model_metrics
from ml.data import process_data

# TODO: implement the first test. Change the function name and input as needed
def test_train():
    """
    # Train model and return the correct type
    """
    x = np.random.rand(20, 5)
    y = np.random.randint(0, 2, 20)

    model = train_model(x, y)
    assert isinstance(model, RandomForestClassifier)
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_metrics():
    """
    # Checks if the expected values are returned
    """
    y_true = [0,1,1,0]
    y_pred = [0,1,0,0]
    
    precision, recall, fbeta = compute_model_metrics(y_true, y_pred)
    
    assert precision == 1.0
    assert recall == 0.5
    assert round(fbeta, 2) == 0.67
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_process_data():
    """
    Check if process_data returns non-empty outputs
    """
    df = pd.DataFrame({
        "workclass": ["Private"],
        "education": ["Some-college"],
        "marital-status": ["Never-married"],
        "occupation": ["Armed-Forces"],
        "relationship": ["Not-in-family"],
        "race": ["White"],
        "sex": ["Female"],
        "native-country": ["United-States"],
        "salary": ["<=50K"]
    })

    cat_features = [
        "workclass", "education", "marital-status", "occupation",
        "relationship", "race", "sex", "native-country"
    ]

    x, y, encoder, lb = process_data(
        df, 
        categorical_features = cat_features, 
        label = "salary",
        training = True  
    )

    assert x is not None
    assert y is not None

    pass
