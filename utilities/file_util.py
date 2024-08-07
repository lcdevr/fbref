import os
import csv

def check_delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)

def open_csv(filepath):
    with open(filepath, mode='r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]
    return data