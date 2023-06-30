'''
Создайте несколько переменных заканчивающихся и не оканчивающихся на "s".
Напишите функцию, которая при запуске заменяет содержимое переменных оканчивающихся на s (кроме переменной из одной буквы s) на None. 
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.
'''
x1 = "hose"
x2 = "second"
x3 = "cassandra"
x4 = "carcass"
x5 = "grass"
x6 = "s"

def replace_with_s(*words):
    words = list(words)
    temp = []
    for i in range(len(words)):
        if words[i].endswith('s') and words[i] != 's':
            words[i] = None
    for i in range(len(words)):
        if words[i] is not None:
            words[i] += ' '.join([i for i in temp])
    return words


print(replace_with_s(x1, x2, x3, x4, x5, x6))