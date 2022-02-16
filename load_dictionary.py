import csv
import random

def get_dictionary(filename):
    dictionary_list = []
    with open(filename, newline='') as csvfile:
        dictreader = csv.reader(csvfile, delimiter=',')
        for row in dictreader:
            for column in row:
                dictionary_list.append(column.lower())
    return dictionary_list