import csv
def re_write(number,value):
    with open('database.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        data = list(csv_reader)
        modified_header = header.copy()
        modified_header[-1] = "class"
        row_to_change = None
        col_to_change = None
        for index, row in enumerate(data):
            if row[0] == str(number):
                row_to_change = index
                col_to_change = len(row)
                break
        if row_to_change is not None:
            data[row_to_change][col_to_change-1] = value

    with open('database.csv', 'w', newline='') as modified_csv_file:
        csv_writer = csv.writer(modified_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(header)
        for row in data:
            csv_writer.writerow(row)
def play_single(number,value):
    with open('playlist.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        data = list(csv_reader)
        modified_header = header.copy()
        row_to_change = None
        col_to_change = None
        for index, row in enumerate(data):
            if row[0] == str(number):
                row_to_change = index
                col_to_change = len(row)
                break
        if row_to_change is not None:
            data[row_to_change][col_to_change-1] = value

    with open('playlist.csv', 'w', newline='') as modified_csv_file:
        csv_writer = csv.writer(modified_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(header)
        for row in data:
            csv_writer.writerow(row)
def del_file():
    with open('playlist.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

    with open('playlist.csv', 'w', newline='') as modified_csv_file:
        csv_writer = csv.writer(modified_csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(header)
