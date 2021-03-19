import csv
import os
from os import listdir, stat
from os.path import isdir, join

import RelativePaths as RP


class DataCollector:
    def __init__(self, data_directory, csv_file_name=str(RP.getRawDataSet())):
        self.data_directory = data_directory
        self.csv_file_name = csv_file_name
        self.field_names = ["FileName", "Label", "FileContent"]
        self.labels = self.collect_labels()
        self.csv_file = None

    def collect_labels(self):
        items = listdir(self.data_directory)
        labels = list(filter(lambda n: isdir(join(self.data_directory, n)), items))
        labels.sort()
        return labels

    def collect_data(self):
        self.read_files_in_data_directory()

    def read_files_in_data_directory(self):
        self.clear_csv_file()
        for label in self.labels:
            self.read_files_in_label_folder(label)

    def read_files_in_label_folder(self, label):
        folder = self.data_directory + "/" + label
        with open(self.csv_file_name, "a", newline="", encoding="UTF-8") as f:
            self.csv_file = csv.DictWriter(f, self.field_names)

            if stat(self.csv_file_name).st_size == 0:
                self.csv_file.writeheader()

            self.add_java_files_in_folder_to_dataset(folder, label)

    def add_java_files_in_folder_to_dataset(self, folder, label):
        if isdir(folder):
            for _file in listdir(folder):
                if _file.endswith(".java"):
                    file_content = self.get_file_content(folder, _file)
                    self.write_to_dataset(_file, label, file_content)
                else:
                    next_folder = "/" + _file
                    self.add_java_files_in_folder_to_dataset(next_folder, label)

    def get_file_content(self, folder, _file):
        file_name = os.path.join(folder, _file)
        with open(file_name, "r", encoding="UTF-8") as f:
            file_content = f.read()
        return file_content

    def write_to_dataset(self, _file, label, file_content):
        self.csv_file.writerow(
            {
                self.field_names[0]: _file,
                self.field_names[1]: label,
                self.field_names[2]: file_content,
            }
        )

    def clear_csv_file(self):
        if os.path.isfile(self.csv_file_name) is True:
            with open(self.csv_file_name, "r+", encoding="UTF-8") as f:
                if stat(self.csv_file_name).st_size != 0:
                    f.truncate()


if __name__ == "__main__":
    jabref_architecture_folder = str(RP.getJabRefDirectory())
    dc = DataCollector(jabref_architecture_folder)
    dc.collect_data()
