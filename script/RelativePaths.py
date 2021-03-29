from pathlib import Path

"""
returns a path object that tells where the file is relative to the current
folder
"""


def getCurrentDirectory():
    return Path.cwd()


def getParentDirectory():
    return Path.cwd().parent


def getJabRefDirectory():
    return getParentDirectory() / "architectures/JabRef_architecture"


def getPromDirectory():
    return getParentDirectory() / "architectures/ProM_architecture"


def getTeamMatesDirectory():
    return getParentDirectory() / "architectures/TEAMMATES_architecture"


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
