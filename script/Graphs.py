import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

NUM_OF_CLASSES_CAP = 6


def plot_horizontal_graphs(metrics: dict, graph_type: str):
    if graph_type == "norm":
        fig, axis = plt.subplots(1, 3, figsize=(20, 5))
        axis[0].set_title(
            metrics["maxEnt"].name + " Normalized Confusion-matrix", fontsize=15
        )
        axis[1].set_title(
            metrics["SVM"].name + " Normalized Confusion-matrix", fontsize=15
        )
        axis[2].set_title(
            metrics["Naive"].name + " Normalized Confusion-matrix", fontsize=15
        )
        fig1 = visualize_normalized_confusion_matrix(metrics["maxEnt"], axis[0])
        fig2 = visualize_normalized_confusion_matrix(metrics["SVM"], axis[1])
        fig3 = visualize_normalized_confusion_matrix(metrics["Naive"], axis[2])
        plt.tight_layout()
        plt.show()
    elif graph_type == "regular":
        fig, axis = plt.subplots(1, 3, figsize=(20, 5))
        axis[0].set_title(metrics["maxEnt"].name + " Confusion-matrix", fontsize=15)
        axis[1].set_title(metrics["SVM"].name + " Confusion-matrix", fontsize=15)
        axis[2].set_title(metrics["Naive"].name + " Confusion-matrix", fontsize=15)
        fig1 = visualize_confusion_matrix(metrics["maxEnt"], axis[0])
        fig2 = visualize_confusion_matrix(metrics["SVM"], axis[1])
        fig3 = visualize_confusion_matrix(metrics["Naive"], axis[2])
        plt.tight_layout()
        plt.show()
    elif graph_type == "report":
        fig, axis = plt.subplots(1, 4, figsize=(24, 6))
        axis[0].set_title(
            metrics["maxEnt"].name + " Classification report", fontsize=18
        )
        axis[1].set_title(metrics["SVM"].name + " Classification report", fontsize=18)
        axis[2].set_title(metrics["Naive"].name + " Classification report", fontsize=18)
        axis[3].set_title("Quantity of files for given concern", fontsize=18)
        fig1 = plot_data_info(metrics["maxEnt"], axis[0])
        fig2 = plot_data_info(metrics["SVM"], axis[1])
        fig3 = plot_data_info(metrics["Naive"], axis[2])
        plot_support_table(metrics["Naive"], axis[3])
        plt.tight_layout()
        plt.show()


# TODO: plot 3 line graphs horizonally, e.g. above, for top three settings
def plot_line_graph(title: str, x_axis, y_axis: dict, x_axis_name, y_axis_name):
    fig = plt.figure(figsize=(8, 8))
    ax1 = fig.add_subplot(111)
    plt.title(title, fontsize=20)
    ax1.set_ylim(0, 1)
    plt.ylabel(y_axis_name, fontsize=15)
    plt.xlabel(x_axis_name, fontsize=15)

    ax1.scatter(x_axis, y_axis["naive"], s=50, c="b", marker="x", label="Naive-Bayes")
    ax1.plot(x_axis, y_axis["naive"], c="b")

    ax1.scatter(x_axis, y_axis["maxEnt"], s=50, c="r", marker="x", label="MaxEnt")
    ax1.plot(x_axis, y_axis["maxEnt"], c="r")

    ax1.scatter(x_axis, y_axis["svm"], s=50, c="g", marker="x", label="SVM")
    ax1.plot(x_axis, y_axis["svm"], c="g")

    plt.legend(loc="upper left")
    plt.show()


# plots the classification report table
def plot_table_info(metrics, axis=None):
    cf_report = metrics.get_classification_report()
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


def plot_support_table(metrics, axis=None):
    table = metrics.quantity_table()
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


def plot_data_info(metrics, axis=None):
    cf_report = metrics.get_classification_report()
    dataFrame = pd.DataFrame(cf_report).transpose()
    dataFrame = dataFrame.drop("support", axis=1)
    numberOfLabels = len(metrics.dataFrame.Label.unique())
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


def plot_predictionScoreAverage(metrics, classifier):
    listofAverage = metrics.getPredictionScoreAverage(classifier)
    listOflabels = metrics.dataFrame.Label.unique()
    listOflabels.sort()
    horizontal_space = 1
    numOfLabels = len(listofAverage)
    numOfFigures = numOfLabels

    # Quickfix for multiple labels
    if NUM_OF_CLASSES_CAP < numOfLabels:
        horizontal_space = 4

    figure = plt.figure(figsize=(15, 15))
    figure.suptitle("Classifier: " + metrics.name, fontsize=15)

    gridspace = figure.add_gridspec(int(numOfFigures), hspace=horizontal_space)
    axes = gridspace.subplots()
    for index in range(int(numOfFigures)):
        averageScore = [item for sublist in listofAverage[index] for item in sublist]
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

        title = metrics.listOfAveragePrediction[index]
        axes[index].set_title(title, pad=12)
        axes[index].set(ylabel="Prediction probability")
    plt.show()


def visualize_normalized_confusion_matrix(metrics, axis=None):
    labels = metrics.dataFrame.Label.unique()
    labels.sort()
    cf_matrix = metrics.get_normalized_confusion_matrix()
    fig = sns.heatmap(
        cf_matrix,
        annot=True,
        yticklabels=labels,
        xticklabels=labels,
        cmap="YlGnBu",
        fmt=".1%",
        ax=axis,
        annot_kws={"size": 10},
    )
    return fig


def visualize_confusion_matrix(metrics, axis=None):
    labels = metrics.dataFrame.Label.unique()
    labels.sort()
    cf_matrix = metrics.get_confusion_matrix()
    fig = sns.heatmap(
        cf_matrix,
        annot=True,
        yticklabels=labels,
        xticklabels=labels,
        cmap="YlGnBu",
        fmt="d",
        ax=axis,
        annot_kws={"size": 10},
    )
    return fig


""" Comandline printing """


def printAll(metrics):
    metrics.printHeader()
    metrics.printMetrics()
    metrics.printStar()


def printHeader(metrics):
    metrics.printStar()
    print(" " * (int((metrics.HeaderLen / 2) - len(metrics.name) / 2)) + metrics.name)
    metrics.printStar()
    print("")
    print("")


def printStar(metrics):
    print("*" * int(metrics.HeaderLen))


def printMetrics(metrics):
    print(
        metrics.confusion_matrix(
            metrics.y_test, metrics.y_pred, metrics.dataFrame.Label.unique()
        )
    )
    print(
        metrics.classification_report(
            metrics.y_test, metrics.y_pred, zero_division=False
        )
    )
    print(
        "Accuracy score:" + str(metrics.accuracy_score(metrics.y_test, metrics.y_pred))
    )
    print("MCC:" + str(metrics.matthews_corrcoef(metrics.y_test, metrics.y_pred)))
