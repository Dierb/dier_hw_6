# 1. Перезаписать все три пройденные алгоритмы в ООП
# стиль ( используя конструктор init и обращение к
# атрибуту через self )
# 2. К таким темам относятся Бинарное дерево ,
# Сортировка Пузырьком , Быстрая сортировка
array = [64, 23, 89, 1, 5, 12, 33]
class Ara:
    def __init__(self,array):
        self.array = array

    def bubble_sort(self):
        swapped = False
        for number_1 in range(len(self.array) -1, 0, -1):
            for number_2 in range(number_1):
                if self.array[number_2] > self.array[number_2 +1]:
                    self.array[number_2], self.array[number_2 +1] = self.array[number_2 + 1], self.array[number_2]
                    swapped = True
            if swapped:
                swapped = False
            else:
                break
        return self.array

    def quick_sort(self, array=None):
        if array == None:
            array = self.array
        if len(array) <= 1:
            return array
        element = array[0]
        left = list(filter(lambda num: num < element , array))
        centr = [nums for nums in array if nums == element]
        right = list(filter(lambda num: num > element , array))

        return self.quick_sort(left) + centr + self.quick_sort(right)

    def binary_tree(self):
        self.array.sort()
        print(self.array)

        desiret_num = int(input('enter the nuber u wont a find'))

        mid = len(self.array) //2
        low = 0
        higt = len(self.array) - 1

        while self.array[mid] != desiret_num and low <= higt:
            if desiret_num > self.array[mid]:
                low = mid +1
            else:
                higt = mid - 1
            mid = (low + higt)//2
        if low > higt:
            print('no value')
        else:
            print('index', mid)

a = Ara(array)
print(a.bubble_sort())
print(a.quick_sort())
print(a.binary_tree())


# Задача # легкий алгоритм
# Смысл задачи: Дается число и если это число можно читать с
# конца до начало и выходит также как и при обратном счете значит
# это число относится к универсальным числам
# 1. Дано число 343 и нужно работать с ним
# 2. Все числа с минусовым значением заведемо считаются не
# универсальными такие как -343
def numbers(number):
    number = str(number)
    if number == number[::-1]:
        return True
    else:
        return False
print(numbers(343))

