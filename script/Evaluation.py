import pandas as pd
import RelativePaths as RP
import Testing

# from sklearn.feature_extraction.text import TfidfVectorizer
# from FeatureRepresentation import FeatureRepresentation
from Classifier import Algorithm, Classifier
from sklearn.feature_extraction.text import CountVectorizer


class Evaluation:

    # fold_quantity splits the dataFrame into 10 folders, 9 of these are used as test data while
    # 1 is used for training. This will be executed in a cross-validator.

    def __init__(
        self,
        dataFrame=None,
        feature_vector=None,
        test_size=None,
        fold_quantity=10,
        numberOfFiles=None,
    ):
        self.dataFrame = dataFrame
        self.f_vector = feature_vector
        self.fold_quantity = fold_quantity
        self.number_of_files_to_test = numberOfFiles
        self.test_size = test_size

    def setDataFrame(self, newData):
        self.dataFrame = newData

    def setFeatureRepresentation(self, feature_vector):
        self.f_vector = feature_vector

    def setFold_quantity(self, fold_quantity):
        self.fold_quantity = fold_quantity

    def evaluate_Naive_Bayes(self, type="standard"):
        best_classifier, classifier_metrics = Testing.evaluate_classifier(
            self.dataFrame,
            classifier=Classifier(Algorithm.NAIVE_BAYES, "Naive-Bayes"),
            feature_representation=self.f_vector,
            fold_quantity=self.fold_quantity,
            test_size=self.test_size,
            type=type,
            number_of_files_for_training=self.number_of_files_to_test,
        )
        return best_classifier, classifier_metrics

    def evaluate_MaxEnt(self, type="standard"):
        best_classifier, classifier_metrics = Testing.evaluate_classifier(
            self.dataFrame,
            classifier=Classifier(Algorithm.MAX_ENT, "MaxEnt"),
            feature_representation=self.f_vector,
            fold_quantity=self.fold_quantity,
            test_size=self.test_size,
            type=type,
            number_of_files_for_training=self.number_of_files_to_test,
        )
        return best_classifier, classifier_metrics

    def evaluate_SVM(self, type="standard"):
        best_classifier, classifier_metrics = Testing.evaluate_classifier(
            self.dataFrame,
            classifier=Classifier(Algorithm.SVM, "SVM"),
            feature_representation=self.f_vector,
            fold_quantity=self.fold_quantity,
            test_size=self.test_size,
            type=type,
            number_of_files_for_training=self.number_of_files_to_test,
        )
        return best_classifier, classifier_metrics


def filter_unwanted_labels(dataFrame, label, val):
    return dataFrame[dataFrame[label].isin(val) == False].reset_index(drop=True)


if __name__ == "__main__":
    dataFrame = pd.read_csv(str(RP.get_basic_preprocessing_csv()))
    dataFrame = filter_unwanted_labels(dataFrame, "Label", ["GLOBALS", "CLI"])
    eval = Evaluation(
        dataFrame, CountVectorizer(), test_size=0.9, fold_quantity=10, numberOfFiles=5
    )
    a, b = eval.evaluate_MaxEnt()
    b.plot_support_table()
