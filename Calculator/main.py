def is_math(a: str) -> bool:
    list_num = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "+", "-", "/", "*"]
    a = list(a)
    for elem in a:
        if elem not in list_num:
            return False
    return True


while True:
    task = input("Высчитать: ")
    if is_math(task):
        print("Результат: "+str(eval(task)))



