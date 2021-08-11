from sklearn.ensemble import GradientBoostingClassifier

def train(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model


if __name__ == '__main__':
    pass