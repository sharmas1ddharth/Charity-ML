import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

def clean_data(data):
    if 'Unnamed: 0' in data.columns:
        data.drop('Unnamed: 0', axis=1, inplace=True)

    # drop null values
    data.dropna(axis=0, inplace=True)

    # dividing data into features and labels

    if 'income' in data.columns:
        y = data['income']
        X = data.drop('income', axis=1)

    else:
        X = data
    # apply logarithmic transformation on skewed data
    skewed = ['capital-gain', 'capital-loss']
    X[skewed] = X[skewed].apply(lambda x: np.log(x+1))

    # normalize data (some columns have larger range than other) using minmax scaler
    # initialize scaler
    scaler = MinMaxScaler()

    # storing numerical cols to list
    numerical_col = [col for col in X.columns if X[col].dtype != 'object']

    # fit and transform numerical data
    X[numerical_col] = scaler.fit_transform(X[numerical_col])

    # one hot encoding
    X = pd.get_dummies(X)

    # label also has categorical columns, encoding '<=50K' as 0 and '>50k' as 1

    if 'income' in data.columns:
        y = y.replace({'<=50K': 0, '>50K' : 1})

        # merge X and y back to one dataset
        data = pd.concat([X, y], axis=1)

        return data

    return X

if __name__ == '__main__':
    pass