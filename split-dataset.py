from sklearn.datasets import load_svmlight_file, dump_svmlight_file
from sklearn.model_selection import train_test_split
import os
import argparse
import gzip


def get_data(dataset):
    data = load_svmlight_file(dataset)
    return data[0], data[1]


def split(dataset, percentage, output_train, output_test):

    X, y = get_data(dataset)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=percentage, random_state=42, stratify=y)

    f_train = gzip.open(output_train,"wb")
    dump_svmlight_file(X_train,y_train,f_train)
    f_train.close()

    f_test = gzip.open(output_test,"wb")
    dump_svmlight_file(X_test,y_test,f_test)
    f_test.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Split dataset train and test')
    parser.add_argument('dataset', help='numpy file with predicted and test classes')
    parser.add_argument('percentage', help='percentage to keep for testing',type=float)

    args = parser.parse_args()

    dataset = args.dataset
    print("Processing dataset {}".format(dataset))
    assert os.path.exists(dataset), "dataset not found"
    percentage = args.percentage / 100.0
    print("Train - Test split: {} - {}".format(1-percentage,percentage))

    if dataset.endswith('.gz'):
        dataset_mod = dataset[:-3]
    else:
        dataset_mod = dataset

    output_train = dataset_mod + ".train.gz"
    output_test = dataset_mod + ".test.gz"
    split(dataset, percentage, output_train, output_test)