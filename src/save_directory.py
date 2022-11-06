import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)

def read_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)


if __name__ == '__main__':
    save_dict({1: 'a', 'b':2, 'c': { 'a': 1}}, 'my_dict.out')
    newDict = read_dict('my_dict.out')
    print(newDict)
    save_dict({1: 'a', 'b':2, 'c': { 'a': 1}}, 'my_dict.txt')