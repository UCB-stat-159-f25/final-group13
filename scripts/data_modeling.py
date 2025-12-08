import numpy as np
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def compute_regression_metrics(y_true, y_pred):
    
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mae = mean_absolute_error(y_true, y_pred)
    mape = np.mean(np.abs((y_true - y_pred) / np.clip(y_true, 1e-8, None))) * 100
    r2 = r2_score(y_true, y_pred)

    return {"RMSE": rmse, "MAE": mae, "MAPE": mape, "R2": r2}



def directional_accuracy(y_true, y_pred):
    
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)

    true_sign = np.sign(y_true)
    pred_sign = np.sign(y_pred)

    return np.mean(true_sign == pred_sign)


def make_lstm_sequences(X_array, y_array, seq_len: int):
    
    X_seq, y_seq = [], []
    n_samples = len(X_array)

    for t in range(seq_len, n_samples):
        X_seq.append(X_array[t-seq_len:t])
        y_seq.append(y_array[t])

    return np.array(X_seq), np.array(y_seq)