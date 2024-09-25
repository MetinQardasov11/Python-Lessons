data_str = 'data string'
data_int = 5
data_list = [11, 22, 33]
data_dict = {'a': 1, 'b': 2}

def tested(word, count=1):
    return word * count

# print(__name__)

if __name__ == '__main__':
    print(tested('hello ', 3))