import enum

from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import MultinomialNB


class Classifier:
    def __init__(self, algo, name):
        self.tag = algo
        self.name = name

    def createObject(self):
        if self.tag == Algorithm.NAIVE_BAYES:
            return MultinomialNB(alpha=0.01)
        if self.tag == Algorithm.SVM:
            return svm.SVC(
                kernel="linear",
                C=1,
                decision_function_shape="ovo",
                probability=True,
                class_weight="balanced",
            )
        if self.tag == Algorithm.MAX_ENT:
            return LogisticRegression(
                multi_class="multinomial", max_iter=1000, class_weight="balanced"
            )

    def getClassifierName(self):
        return self.name


class Algorithm(enum.Enum):
    NAIVE_BAYES = 1
    MAX_ENT = 2
    SVM = 3
