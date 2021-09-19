import itertools
import string


class Possible_combinations():
    def __init__(self):
        self.user_input()
        self.tmp_list()
        self.print_result()

    def user_input(self):
        print('Keyword generator:\n\nB-большие буквы\nL-маленькие буквы\nS-спецсимволы\nN-числа')
        self.args = set(input('Выберите аргументы: ').lower()) & {'b', 'l', 'n', 's'}
        self.length = int(input('Введите количество символов '))

    def tmp_list(self):
        combination_dict = {'b': string.ascii_uppercase, 'l': string.ascii_lowercase, 's': string.punctuation, \
                            'n': string.digits}
        self.combination = ''.join([combination_dict[i.lower()] for i in self.args])
        combinations = itertools.product(self.combination, repeat=self.length)
        list_of_combinations = []
        for i in combinations:
            list_of_combinations.append(i)
            if len(list_of_combinations) == 100:
                self.writefile(list_of_combinations)
                list_of_combinations = []

    def writefile(self, list):
        with open('my_dict.txt', 'a', encoding="UTF-8") as file:
            for i in list:
                file.write(''.join(i) + '\n')

    def print_result(self):
        print(f"{len(self.combination) ** self.length}\nDone")


mypossible_combinations = Possible_combinations()
