import numpy as np
import pytest
from scripts.data_modeling import compute_regression_metrics, directional_accuracy

# This tests the test metrics are correct while prediction perfectly matches actual. 
def test_compute_regression_metrics():
    y_real = [1.0, 1.0, 3.0, 4.0]
    y_pred = [1.0, 1.0, 3.0, 4.0]

    final_output = compute_regression_metrics(y_real, y_pred)

    assert final_output["MAE"] == 0
    assert final_output["R2"] == 0
    assert final_output["RMSE"] == 0


# This tests that the calculation of direction is accurate/correct. 
def test_directional_accuracy():
    y_real = [1, -1, 1, -1]
    y_pred = [1, 2, 3, 4]

    #This should match 2 as positive signs match positive signs in only two places

    correctness = directional_accuracy(y_real, y_pred)

    assert correctness == 0.5


    




