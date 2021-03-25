import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    matthews_corrcoef,
    precision_score,
    recall_score
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

    def get_Y_test(self):
        return self.y_test

    def get_Y_pred(self):
        return self.y_pred

    def get_classifier_name(self):
        return self.name

    def get_X_test(self):
        return self.X_test

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
        return precision_score(self.y_test, self.y_pred, average="macro")

    def get_accuracy_score(self):
        return accuracy_score(self.y_test,self.y_pred)

    def get_recall_score(self):
        return recall_score(self.y_test,self.y_pred, average="macro")


    # plots the classification report table
    def plot_table_info(self, axis=None):
        cf_report = self.get_classification_report()
        df = pd.DataFrame(cf_report).transpose()
        df = df.round(decimals=2)
        header = ["Concerns", "Precision", "Recall", "f1-score", "Support"]
        pandasList = df.values.tolist()
        currPos = 0
        for list in pandasList:
            list.insert(0, df.iloc[currPos].name)
            currPos += 1
        pandasList.insert(0, header)

        table = plt.table(cellText=pandasList, loc="center")
        table.set_fontsize(12)
        table.scale(1, 1)

        for row in range(len(header)):
            table[0, row].get_text().set_fontsize(20)
            table[0, row].get_text().set_fontweight("bold")
        for col in range(len(cf_report) + 1):
            table[col, 0].get_text().set_fontsize(20)
            table[col, 0].get_text().set_fontweight("bold")
        plt.axis("off")
        plt.show()
        return table

    def plot_support_table(self, axis=None):
        table = self.quantity_table()
        sns.heatmap(
            table,
            cmap="YlGnBu",
            annot=True,
            linewidths=0.5,
            fmt="d",
            ax=axis,
            annot_kws={"size": 15},
        )
        plt.show()
        return

    def quantity_table(self):
        cf_report = self.get_classification_report()
        df = pd.DataFrame(cf_report).transpose()
        dfSupport = df.drop(["accuracy", "macro avg", "weighted avg"])
        dfSupport = dfSupport.support

        numOfLabels = self.dataFrame.Label.count()
        print(numOfLabels)
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

    def plot_data_info(self, axis=None):
        cf_report = self.get_classification_report()
        dataFrame = pd.DataFrame(cf_report).transpose()
        dataFrame = dataFrame.drop("support", axis=1)
        numberOfLabels = len(self.dataFrame.Label.unique())
        grid = np.zeros((numberOfLabels + 3, 4))
        grid[:, 3] = True  # support
        sns.heatmap(
            dataFrame,
            cmap="YlGnBu",
            annot=True,
            linewidths=0.5,
            ax=axis,
            annot_kws={"size": 15},
        )
        return None

    def plot_predictionScoreAverage(self, classifier):
        listofAverage = self.getPredictionScoreAverage(classifier)
        listOflabels = self.dataFrame.Label.unique()
        listOflabels.sort()
        numOfLabels = len(listofAverage)
        numOfFigures = numOfLabels

        figure = plt.figure(figsize=(10, 10))
        figure.suptitle("Classifier: "+self.name,fontsize = 28)
        gridspace = figure.add_gridspec(int(numOfFigures), hspace=1)
        axes = gridspace.subplots()
        for index in range(int(numOfFigures)):
            averageScore = [
                item for sublist in listofAverage[index] for item in sublist
            ]
            fig = axes[index].bar(listOflabels, averageScore, width=0.25, color="red")
            axes[index].set_ylim([0, 100])
            for bar in fig:
                height = bar.get_height()
                axes[index].text(
                    bar.get_x() + bar.get_width() / 2.0,
                    1.05 * height,
                    "%.1f" % round(float(height), 1) + "%",
                    ha="center",
                    va="bottom",
                )

            title = self.listOfAveragePrediction[index]
            axes[index].set_title(title, pad=12, fontsize=20)
            axes[index].set(ylabel="Prediction probability")
        plt.show()

    def visualize_normalized_confusion_matrix(self, axis=None):
        labels = self.dataFrame.Label.unique()
        labels.sort()
        cf_matrix = self.get_normalized_confusion_matrix()
        fig = sns.heatmap(
            cf_matrix,
            annot=True,
            yticklabels=labels,
            xticklabels=labels,
            cmap="YlGnBu",
            fmt=".1%",
            ax=axis,
            annot_kws={"size": 15},
        )
        return fig

    def visualize_confusion_matrix(self, axis=None):
        labels = self.dataFrame.Label.unique()
        labels.sort()
        cf_matrix = self.get_confusion_matrix()
        fig = sns.heatmap(
            cf_matrix,
            annot=True,
            yticklabels=labels,
            xticklabels=labels,
            cmap="YlGnBu",
            fmt="d",
            ax=axis,
        )
        return fig

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

    """ Comandline printing """

    def printAll(self):
        self.printHeader()
        self.printMetrics()
        self.printStar()

    def printHeader(self):
        self.printStar()
        print(" " * (int((self.HeaderLen / 2) - len(self.name) / 2)) + self.name)
        self.printStar()
        print("")
        print("")

    def printStar(self):
        print("*" * int(self.HeaderLen))

    def printMetrics(self):
        print(confusion_matrix(self.y_test, self.y_pred, self.dataFrame.Label.unique()))
        print(classification_report(self.y_test, self.y_pred, zero_division=False))
        print("Accuracy score:" + str(accuracy_score(self.y_test, self.y_pred)))
        print("MCC:" + str(matthews_corrcoef(self.y_test, self.y_pred)))
