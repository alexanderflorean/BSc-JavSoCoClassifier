


def filter_unwanted_labels(dataFrame, val):
    return dataFrame[dataFrame['Label'].isin(val) == False].reset_index(drop=True)


def remove_concerns_under_quantity_threshold(dataFrame, minNumOfFiles=10):
    labels = dataFrame.Label.unique()
    x_quantity = [len(dataFrame.loc[dataFrame['Label'] == label]) for label in labels]
    to_be_removed_labels = []
    for pos in range(len(labels)):
        if x_quantity[pos] < minNumOfFiles:
            to_be_removed_labels.append(labels[pos])

    return filter_unwanted_labels(dataFrame, to_be_removed_labels)
