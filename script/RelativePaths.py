from pathlib import Path


# Returns path object, needs to converted to string to be used
def getCurrentDirectory():
    return Path.cwd()


def getParentDirectory():
    return Path.cwd().parent


def getJabRefDirectory():
    return getParentDirectory() / "JabRef_architecture"


def getDataDirectory():
    return getParentDirectory() / "Data"


def getRawDataSet():
    return getDataDirectory() / "rawData.csv"


def get_processed_dataset():
    return getDataDirectory() / "processedData.csv"


def get_basic_preprocessing_csv():
    return getDataDirectory() / "basic_preprocessing.csv"


def get_type1_processed_csv():
    return getDataDirectory() / "type1_preprocessing.csv"
