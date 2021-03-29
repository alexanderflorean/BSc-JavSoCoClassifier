import numpy as np
import pandas as pd
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    precision_score,
    recall_score,
)


class Metric:
    """
    Both extracts relevant metrics and plots them
    """

    # for the command line printing
    HeaderLen = 60

    def __init__(
        self, y_test=None, y_pred=None, X_test=None, Name=None, dataFrame=None
    ):
        self.y_test = y_test
        self.y_pred = y_pred
        self.X_test = X_test
        self.name = Name
        self.dataFrame = dataFrame
        self.listOfAveragePrediction = []

    def get_classifier_name(self):
        return self.name

    def get_normalized_confusion_matrix(self):
        return confusion_matrix(self.y_test, self.y_pred, normalize="true")

    def get_confusion_matrix(self):
        return confusion_matrix(self.y_test, self.y_pred)

    def get_classification_report(self):
        labels = self.dataFrame.Label.unique()
        labels.sort()
        return classification_report(
            self.y_test,
            self.y_pred,
            zero_division=False,
            target_names=labels,
            output_dict=True,
        )

    def get_precision_score(self):
        return precision_score(
            self.y_test, self.y_pred, average="macro", zero_division=False
        )

    def get_accuracy_score(self):
        return accuracy_score(self.y_test, self.y_pred)

    def get_recall_score(self):
        return recall_score(
            self.y_test, self.y_pred, average="macro", zero_division=False
        )

    def quantity_table(self):
        cf_report = self.get_classification_report()
        df = pd.DataFrame(cf_report).transpose()
        dfSupport = df.drop(["accuracy", "macro avg", "weighted avg"])
        dfSupport = dfSupport.support

        label = self.dataFrame.Label.unique()
        label.sort()
        y_labels = self.dataFrame.Label.unique()
        label_quantities = [
            len(self.dataFrame.loc[self.dataFrame["Label"] == label])
            for label in y_labels
        ]
        train_quantity = np.subtract(label_quantities, dfSupport.to_list())
        table = pd.DataFrame(
            {
                "Test": map(int, dfSupport.to_list()),
                "Train": map(int, train_quantity),
                "Total": label_quantities,
            },
            index=y_labels,
        )
        return table

    def getPredictionScoreAverage(self, classifier):
        listOfLabels = self.dataFrame.Label.unique()
        listOfLabels.sort()
        numOfLabels = self.y_test.value_counts()
        label_sizes = []
        for label in listOfLabels:
            label_sizes.append(numOfLabels[label])

        indexList = [
            [0 for x in range(max(label_sizes))] for y in range(len(listOfLabels))
        ]
        for k in range(len(listOfLabels)):
            outOfBounds = 0
            for index, label in enumerate(self.y_test):
                if outOfBounds < label_sizes[k]:
                    if listOfLabels[k] == label:
                        indexList[k][outOfBounds] = index
                        outOfBounds += 1
                else:
                    break

        arr = self.y_test.to_numpy()
        arrContent = self.X_test
        listOfAverages = []
        for i in range(len(listOfLabels)):
            temp = np.full((1, len(listOfLabels)), 0)
            for j in range(label_sizes[i]):
                if j > 0 and arr[indexList[i][j]] == 0:
                    break
                else:
                    result = classifier.predict_proba(arrContent[indexList[i][j]])
                    temp = np.add(temp, result)
            temp = np.divide(temp, label_sizes[i])
            temp = np.multiply(temp, 100)
            listOfAverages.append(temp)
        for i in range(len(listOfLabels)):
            self.listOfAveragePrediction.append(
                "Average of "
                + str(label_sizes[i])
                + " "
                + listOfLabels[i]
                + " classes (%)"
            )

        return listOfAverages

    def total_report_table(self):
        """
        Appends the quantities of labels to the classification report table
        """
        classification_report = pd.DataFrame(self.get_classification_report())
        quantity_table = self.quantity_table()
        quantity_table = quantity_table.transpose()
        total_df = classification_report.append(quantity_table)
        return total_df
