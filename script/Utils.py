import yaml

MIN_NUM_OF_TEST_FILES = 5  # minimum of available 5 test files regardless of training size.


def filter_unwanted_labels(dataFrame, val):
    return dataFrame[dataFrame['Label'].isin(val) == False].reset_index(drop=True)


def remove_concerns_under_quantity_threshold(dataFrame, minNumOfFiles=5):
    labels = dataFrame.Label.unique()
    x_quantity = [len(dataFrame.loc[dataFrame['Label'] == label]) for label in labels]
    to_be_removed_labels = []
    for pos in range(len(labels)):
        if x_quantity[pos] < minNumOfFiles + MIN_NUM_OF_TEST_FILES:
            to_be_removed_labels.append(labels[pos])

    return filter_unwanted_labels(dataFrame, to_be_removed_labels)


def read_yaml_file(path_to_yaml: str):
    try:
        with open(path_to_yaml, 'r') as file:
            config = yaml.safe_load(file)
            return config
    except Exception as e:
        print(e + ': Error reading the yaml file')


def make_dataframe_row(metrics, setting: list, setting_id: str) -> dict:
    report = metrics.get_classification_report()
    quantity_table = metrics.quantity_table()
    row = {
        'classifier': metrics.name,
        'setting_id': setting_id,
        'settings': setting,
        'accuracy': report['accuracy'],
        'w_avg_precision': report['weighted avg']['precision'],
        'w_avg_recall': report['weighted avg']['recall'],
        'train_size': quantity_table['Train'].sum(),
        'test_size': quantity_table['Test'].sum(),
        'report_table': metrics.total_report_table()
    }
    return row
