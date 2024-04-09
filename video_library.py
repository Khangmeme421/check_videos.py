from library_item import LibraryItem
import csv

class PlayList(LibraryItem):
    def __init__(self, name, director, rating=0,key=''):
        super().__init__(name, director, rating)
        self.key = key

    def play(self):
        self.play_count += 1
        library[self.key].play_count = self.play_count

    def remove_item(self):
        self.play_count = 0
        library[self.key].play_count = self.play_count

#open database file and put data to list
with open('database.csv', newline='\n', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)
    next(csv_reader)

    library = {}
    tmplist = [None] * 4
    for row in csv_reader:
        try:
            len_tmp = 0
            for i in row:
                tmplist[len_tmp] = i
                len_tmp += 1
            library[str(tmplist[0])] = LibraryItem(tmplist[1], tmplist[2], int(tmplist[3]))
        except IndexError:
            pass


def list_all(arr):
    output = ""
    for key in arr:
        item = arr[key]
        output += f"{key} {item.info()}\n"
    return output


def get_name(key,arr):
    try:
        item = arr[key]
        return item.name
    except KeyError:
        return None


def get_director(key,arr):
    try:
        item = arr[key]
        return item.director
    except KeyError:
        return None


def get_rating(key,arr):
    try:
        item = arr[key]
        return item.rating
    except KeyError:
        return -1


def set_rating(key,arr, rating):
    try:
        item = arr[key]
        item.rating = rating
    except KeyError:
        return


def get_play_count(key,arr):
    try:
        item = arr[key]
        return item.play_count
    except KeyError:
        return -1


def increment_play_count(key,arr):
    try:
        item = arr[key]
        item.play_count += 1
    except KeyError:
        return 0

def reset_play_count(key,arr):
    try:
        item = arr[key]
        item.play_count = 0
    except KeyError:
        return 0

