from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.feature_selection import SelectKBest, chi2, f_classif, mutual_info_classif


# TODO:fixa så att splitta träniningsdata först, sen transformera till vector!
class FeatureRepresentation:
    def __init__(
        self, dataFrame_X=None, dataFrame_Y=None, feature_Vector=CountVectorizer()
    ):
        self.feature_representation = feature_Vector
        self.X = dataFrame_X
        self.Y = dataFrame_Y
        self.f_vector = None

    def createCountVector(self):
        self.feature_representation = CountVectorizer()

    def createTFidVector(self, tf_id=False):
        self.feature_representation = TfidfVectorizer(use_idf=tf_id)

    def getFeatureVector(self, X_data):
        return self.feature_representation.fit_transform(X_data)

    def getX_Y(self):
        return self.f_vector, self.Y

    def featureSelectionKbestCHI(self, num_features):
        self.f_vector = SelectKBest(chi2, k=num_features).fit_transform(
            self.f_vector, self.Y
        )

    def featureSelectionKbestMutual(self, num_features):
        self.f_vector = SelectKBest(mutual_info_classif, num_features).fit_transform(
            self.f_vector, self.Y
        )

    def featureSelectionKbestf_classif(self, num_features):
        self.f_vector = SelectKBest(f_classif, num_features).fit_transform(
            self.f_vector, self.Y
        )
