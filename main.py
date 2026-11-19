print("--------------------------------------------------------")
print("------------------Калькулятор---------------------------")
print("--------------------------------------------------------")
while True:
    hd = input("Какое действие? (+, -, *, /, Стоп): ")
    if hd == "Стоп":
        break
    if hd not in ("+", "-", "*", "/"):
        print("Не правильное действие!!!!")
        continue
    try:
        h1 = float(input("Напишите 1 число: "))
        h2 = float(input("Напишите 2 число: "))
        if hd == "+":
            Ot = h1 + h2
        elif hd == "-":
            Ot = h1 - h2
        elif hd == "*":
            Ot = h1 * h2
        else:
            Ot = h1 / h2
        print(f"{h1:g} {hd} {h2:g} = {Ot:g}")
    except ZeroDivisionError:
        print("Нельзя делить на 0!!!")
    except ValueError:
        print("Нужно ввести число!!!")