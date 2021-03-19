import csv
import os


class DataSet:
    fields = ["FileName", "Label", "FileContent"]

    def __init__(self, path, label, FileName):
        self.csvFile = None
        with open(FileName, "a", newline="", encoding="UTF-8") as f:
            if os.stat(FileName).st_size == 0:
                self.csvFile = csv.DictWriter(f, fieldnames=self.fields)
                self.csvFile.writeheader()
                self.readDirectory(path, label)
            else:
                self.csvFile = csv.DictWriter(f, fieldnames=self.fields)
                self.readDirectory(path, label)

    def readDirectory(self, path, label):
        if self.csvFile is not None:
            for file in os.listdir(path):
                if file.endswith(".java"):
                    print(path + "/" + file)
                    self.csvFile.writerow(
                        {
                            self.fields[0]: file,
                            self.fields[1]: label,
                            self.fields[2]: open(
                                path + "/" + file, encoding="UTF-8"
                            ).read(),
                        }
                    )
                else:
                    self.readDirectory(path + "/" + file, label)
