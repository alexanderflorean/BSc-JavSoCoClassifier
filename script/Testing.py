import pandas as pd
from Metrics import Metric
from sklearn.model_selection import StratifiedShuffleSplit


def evaluate_classifier(
    dataFrame,
    classifier,
    feature_representation,
    fold_quantity,
    type,
    test_size=0.9,
    number_of_files_for_training=5,
):
    if type == "standard":
        return evaluate_classifier_standard(
            dataFrame, classifier, feature_representation, fold_quantity, test_size
        )
    elif type == "custom":
        return evaluate_classifier_custom(
            dataFrame, classifier, feature_representation, number_of_files_for_training
        )


def evaluate_classifier_standard(
    dataFrame, classifier, feature_representation, fold_quantity, test_size
):
    y = dataFrame.Label
    X = dataFrame.FileContent

    listOfClassifier = []
    listOfAccur = []
    classifierMetrics = []
    currPos = 0
    skf = StratifiedShuffleSplit(
        n_splits=fold_quantity, test_size=test_size, random_state=42
    )
    for index_train, index_test in skf.split(X, y):
        x_train_fold, x_test_fold = X[index_train], X[index_test]
        y_train_fold, y_test_fold = y[index_train], y[index_test]
        X_transformer_train = feature_representation.fit_transform(x_train_fold)
        X_transformer_test = feature_representation.transform(x_test_fold)
        listOfClassifier.append(classifier.createObject())
        listOfClassifier[currPos].fit(X_transformer_train, y_train_fold)
        y_pred = listOfClassifier[currPos].predict(X_transformer_test)
        classifierMetrics.append(
            Metric(
                y_test_fold,
                y_pred,
                X_transformer_test,
                classifier.getClassifierName(),
                dataFrame,
            )
        )
        listOfAccur.append(
            listOfClassifier[currPos].score(X_transformer_test, y_test_fold)
        )
        currPos += 1
    # positionOfMinVal = listOfAccur.index(min(listOfAccur))
    positionOfMaxVal = listOfAccur.index(max(listOfAccur))
    return listOfClassifier[positionOfMaxVal], classifierMetrics[positionOfMaxVal]


def evaluate_classifier_custom(
    dataFrame, classifier, feature_representation, number_of_files_for_training
):
    """
    Pre: The number of files chosen should not exceed the number of actual existing files in the system,
    this test is done to simulate real scenario where someone wants to take a portion of files (evenly)
    and map to corresponding label
    """

    x_train, x_test, y_train, y_test = train_fold_quantity_custom(
        dataFrame, number_of_files_for_training
    )

    X_transformer_train = feature_representation.fit_transform(x_train)
    X_transformer_test = feature_representation.transform(x_test)
    model = classifier.createObject()
    model.fit(X_transformer_train, y_train)
    y_pred = model.predict(X_transformer_test)
    metric = Metric(
        y_test, y_pred, X_transformer_test, classifier.getClassifierName(), dataFrame
    )
    return model, metric


def train_fold_quantity_custom(dataFrame, number_of_files_for_training, random_state=0):
    listOfLabels = dataFrame.Label.unique()
    listOfLabels.sort()
    TrainingFrame = pd.DataFrame(columns=dataFrame.columns)
    for currLabel in listOfLabels:
        currentLabelFrame = dataFrame.loc[dataFrame["Label"] == currLabel]
        selectedFrame = currentLabelFrame.sample(
            number_of_files_for_training, random_state=random_state
        )
        TrainingFrame = TrainingFrame.append(selectedFrame, ignore_index=True)
        indexArray = selectedFrame.index.tolist()
        dataFrame = dataFrame.drop(indexArray)

    dataFrame = dataFrame.reset_index()  # Uppdaterar index, startar från 0

    x_train = TrainingFrame["FileContent"]
    y_train = TrainingFrame["Label"]

    x_test = dataFrame["FileContent"]
    y_test = dataFrame["Label"]
    return x_train, x_test, y_train, y_test
