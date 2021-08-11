import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# function to preprocess data and convert it into useful features
def raw_to_data(input):
    columns = ['age', 'workclass', 'fnlwgt', 'education_level', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 
    'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']

    data = pd.read_csv(input)
    data.columns = columns
    data.drop('fnlwgt', axis=1, inplace=True)
    # apply logarithmic transformation on skewed data
    skewed = ['capital-gain', 'capital-loss']
    data[skewed] = data[skewed].apply(lambda x: np.log(x+1))

    # normalize data (some columns have larger range than other) using minmax scaler
    # initialize scaler
    scaler = MinMaxScaler()

    # storing numerical cols to list
    numerical_col = [col for col in data.columns if data[col].dtype != 'object']

    # fit and transform numerical data
    data[numerical_col] = scaler.fit_transform(data[numerical_col])

    # convert categorical columns to numerical
    # one hot encoding
    X = data.drop('income', axis=1)
    y = data['income']

    X = pd.get_dummies(X)
    y = y.replace({'<=50K': 0, '>50K' : 1})
    data = pd.concat([X, y], axis=1)
    return data


if __name__ == '__main__':
    pass


