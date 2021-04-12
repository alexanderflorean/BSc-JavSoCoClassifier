import csv
import os
from os import listdir, stat
from os.path import isdir, join


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


def read_files_to_csv(path, label, csv_file):
    if csv_file is not None:
        for _file in listdir(path):
            if _file.endswith(".java"):
                file_content = get_file_content(path, _file)
                write_to_dataset(csv_file, _file, label, file_content)
            elif isdir(path + "/" + _file):
                read_files_to_csv(path + "/" + _file, label, csv_file)


def get_field_names():
    return ["FileName", "Label", "FileContent"]


def collect_data(path, label, save_file):
    csv_file_name = save_file
    field_names = get_field_names()
    with open(csv_file_name, "a", newline="", encoding="UTF-8") as f:
        csv_file = csv.DictWriter(f, field_names)

        if stat(csv_file_name).st_size == 0:
            csv_file.writeheader()

        read_files_to_csv(path, label, csv_file)


# Removes the file if the file is not empty
def truncate_csv_file(save_file):
    if os.path.isfile(save_file) is True:
        with open(save_file, "r+", encoding="UTF-8") as f:
            if stat(save_file).st_size != 0:
                f.truncate()


def gather_data_from_directory(path, labels, save_file):
    truncate_csv_file(save_file)
    for label in labels:
        directory = path + "/" + label
        collect_data(directory, label, save_file)


def gather_labels_from_folder_names(path):
    """ Returns a list of first level foldernames from chosen directory """
    items = listdir(path)
    labels = [folder for folder in items if isdir(join(path, folder))]
    labels.sort()
    return labels


def gather_architectural_concerns_data(folder, save_file):
    """
    Is the method called upon to gather the data.

    Pre: folder, the folder which contains the given software architectural
    concerns and their assigned files.
    save_file, file name and path to save the results in.
    Post: saves a table of known data for training and testing.
    """
    labels = gather_labels_from_folder_names(folder)
    gather_data_from_directory(folder, labels, save_file)
