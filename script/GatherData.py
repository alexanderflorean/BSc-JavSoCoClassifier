import csv
import os
from os import listdir, stat
from os.path import isdir, join

import RelativePaths as RP


def collect_data(path, label):
    csv_file_name = get_raw_data_file_name()
    field_names = get_field_names()
    with open(csv_file_name, "a", newline="", encoding="UTF-8") as f:
        csv_file = csv.DictWriter(f, field_names)

        if stat(csv_file_name).st_size == 0:
            csv_file.writeheader()

        read_files_to_csv(path, label, csv_file)


def read_files_to_csv(path, label, csv_file):
    if csv_file is not None:
        for _file in listdir(path):
            if _file.endswith(".java"):
                file_content = get_file_content(path, _file)
                write_to_dataset(csv_file, _file, label, file_content)
            elif(isdir(path + "/" + _file)):
                read_files_to_csv(path + "/" + _file, label, csv_file)


def write_to_dataset(csv_file, _file, label, file_content):
    field_names = get_field_names()
    csv_file.writerow(
        {field_names[0]: _file, field_names[1]: label, field_names[2]: file_content}
    )


# returns file content of given path and the filename
def get_file_content(path, _file):
    file_name = os.path.join(path, _file)
    with open(file_name, "r", encoding="UTF-8") as f:
        file_content = f.read()
    return file_content


def gather_jabref_data():
    jabrefDir = RP.getJabRefDirectory()
    labels = gather_labels_from_folder_names(jabrefDir)
    gather_data_from_directory(jabrefDir, labels)


def gather_prom_data():
    prom_dir = RP.getPromDirectory()
    labels = gather_labels_from_folder_names(prom_dir)
    gather_data_from_directory(prom_dir, labels)


def gather_team_mates_data():
    team_dir = RP.getTeamMatesDirectory()
    labels = gather_labels_from_folder_names(team_dir)
    gather_data_from_directory(team_dir, labels)


def gather_data_from_directory(path, labels):
    update_csv_file()
    for label in labels:
        directory = str(path / label)
        collect_data(directory, label)


# Removes the file if the file is not empty
def update_csv_file():
    file_name = get_raw_data_file_name()
    if os.path.isfile(file_name) is True:
        with open(file_name, "r+", encoding="UTF-8") as f:
            if stat(file_name).st_size != 0:
                f.truncate()


def gather_labels_from_folder_names(path):
    """ Returns a list of first level foldernames from chosen directory """
    items = listdir(path)
    labels = [folder for folder in items if isdir(join(path, folder))]
    labels.sort()
    return labels


def get_raw_data_file_name():
    return str(RP.getRawDataSet())


def get_field_names():
    return ["FileName", "Label", "FileContent"]


if __name__ == "__main__":
    gather_jabref_data()
