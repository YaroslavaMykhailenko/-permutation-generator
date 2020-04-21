from sys import exit

def makelst(): # Создание списка с возрастающим порядком. Начальное направление - налево (0).
    lst = []
    try: #Попытка словить ошибку типа данных. (Если введём букву вместо интеджера)
        n = int(input("Введите количество элементов:\n> "))
        for i in range(1, n+1): # Перебор всех элементов
            lst.append([i, 0]) # Тут присваиваются по сути те же значения, которые являются номерами элементов в списке. Но мы делаем 1, n+1 потому что нас интересуют элементы с 1, а номера начинаются с 0
        getAllPermutations(lst) # Функция, которая сделает грязное дело по перестановке всех введённых нами чисел
    except ValueError as a: # Вывод в случае если мы введём бред вместо цифры, в самом начале
        print("Ошибка значения : ", a)
        exit(0)


def changeDirections(lst, MI): # Функция, которая меняет направление перебора

    for element in lst: # Перебираем все элмемнты

        if element[0] > lst[MI][0]: # Сама смена

            if element[1] == 0: # если налево то направо
                element[1] = 1

            elif element[1] == 1: # если направо то налево
                element[1] = 0




def swap(lst, MI): # Обычная функция замены двух рядомстоящих симвлов

    if lst[MI][1] == 0: # Здесь поскольку 0, то меняем символ слева, используя вспомогательный элемент
        tmpElement = lst[MI-1] # MI-1 это позиция слева от текущего, присваиваем значение этой позиции нашему вспомогательному элементу
        lst[MI-1] = lst[MI] # Присваиваем левой позиции значение изначальной позиции
        lst[MI] = tmpElement # А на место изначальной ставим то, что было слева
    elif lst[MI][1] == 1: # Здесь поскольку 1, то меняем символ справа, механизм абсолютно такой же что и сверху
        tmpElement = lst[MI+1]
        lst[MI+1] = lst[MI]
        lst[MI] = tmpElement





def findLargestMI(lst): # Ищем наибольшее

    MI = None # Текущий элемент
    foundMI = False # Искомый наибольший элемент
    for i in lst: # Перебираем содержимое нашего листа

        if i[1] == 0: # Если направление идёт налево, то

            if lst.index(i) != 0:
                    if MI == None: # Это будет при первой итерации, ибо оно не найдёт 1 элемент
                        if i[0] > lst[lst.index(i) - 1][0]: # если текущий элемент больше чем сосед слева, то мы говорим что нашли искомый
                            MI = lst.index(i)
                            foundMI = True

                    elif MI != None:
                        if ( i[0] > lst[lst.index(i) - 1][0] ) and ( i[0] > lst[MI][0] ): # Если больше соседа слева и больше чем наш элемент
                            MI = lst.index(i)
                            foundMI = True


        if i[1] == 1: # Если направление направо
            # То же самое что и с левым направлением, только замены идут в другую сторону
            if lst.index(i) != lst.index(lst[-1]):
                    if MI == None:
                        if i[0] > lst[lst.index(i) + 1][0]:
                            MI = lst.index(i)
                            foundMI = True

                    elif MI != None:
                        if ( i[0] > lst[lst.index(i) + 1][0]) and ( i[0] > lst[MI][0]):
                            MI = lst.index(i)
                            foundMI = True

    if not foundMI: # Если невозможно найти наш искомый элемент, то возвращаем None
        return foundMI

    return MI # Возврат искомого

def getAllPermutations(lst):
    index = 1
    while True:
        printlstWithDirections(lst, index) # принт первого перебора
        index += 1 # счётчик итераций
        MI = findLargestMI(lst) # Снова ищем наибольшее
        if isinstance(MI, bool) and MI == False: # Если возвращается значение False, то мы даём команду на выход и принт энда (условие выхода из while True)
            print("END")
            break # Выход
        changeDirections(lst, MI) # Смена направлений
        swap(lst, MI) # Меняем местами в зависимости от направления
    input()


def printlstWithDirections(lst, index): # Обычный вывод списка, путём переборов элементов
    output = ""
    secondPrint = False
    for i in lst:
        if secondPrint: # Пробельчики
            output += (" ")
        else:
            secondPrint = True

        if i[1] == 0: # Если направление налево, то даём стрелочку налево
            output += ("<" + str(i[0]))
        elif i[1] == 1: # Если направо, то направо
            output += (str(i[0]) + ">")

    print(output)


makelst()