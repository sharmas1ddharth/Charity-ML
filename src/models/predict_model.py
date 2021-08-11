from sklearn.metrics import accuracy_score


def predict(trained_model, data_to_predict, true_value):
    pred = trained_model.predict(data_to_predict)
    accuracy = accuracy_score(true_value, pred)
    return accuracy


if __name__ == '__main__':
    pass