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

)
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import plot_confusion_matrix
import Evaluation as Eva
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

def testing_test_size(dataFrame, test_size):
    fold_quantity = 10
    feature_representation = CountVectorizer()
    # Train and gather evaluation metrics
    evaluate = Eva.Evaluation(dataFrame, feature_representation, test_size,fold_quantity)
    classifier_max_ent, metrics_max_ent = evaluate.evaluate_MaxEnt()
    classifier_svm, metrics_svm = evaluate.evaluate_SVM()
    classifier_naive, metrics_naive = evaluate.evaluate_Naive_Bayes()

    fig, axis = plt.subplots(1, 3, figsize=(15, 5))
    axis[0].set_title(metrics_max_ent.name + " Normalized Confusion-matrix", fontsize=15)
    axis[1].set_title(metrics_svm.name + " Normalized Confusion-matrix", fontsize=15)
    axis[2].set_title(metrics_naive.name + " Normalized Confusion-matrix", fontsize=15)
    fig1 = metrics_max_ent.visualize_normalized_confusion_matrix(axis[0])
    fig2 = metrics_svm.visualize_normalized_confusion_matrix(axis[1])
    fig3 = metrics_naive.visualize_normalized_confusion_matrix(axis[2])
    plt.tight_layout()
    plt.show()

    fig, axis = plt.subplots(1, 4, figsize=(18, 5))
    axis[0].set_title(metrics_max_ent.name + " Classification report", fontsize=15)
    axis[1].set_title(metrics_svm.name + " Classification report", fontsize=15)
    axis[2].set_title(metrics_naive.name + " Classification report", fontsize=15)
    axis[3].set_title("Quantity", fontsize=15)
    fig1 = metrics_max_ent.plot_data_info(axis[0])
    fig2 = metrics_svm.plot_data_info(axis[1])
    fig3 = metrics_naive.plot_data_info(axis[2])
    metrics_naive.plot_support_table(axis[3])
    plt.tight_layout()
    plt.show()

    metrics_max_ent.plot_predictionScoreAverage(classifier_max_ent)
    metrics_naive.plot_predictionScoreAverage(classifier_naive)
    metrics_svm.plot_predictionScoreAverage(classifier_svm)



def testing_custom_size(dataFrame,num_of_file):
    pass
