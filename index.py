city1 = "Москва - Россия - 12500000"
city2 = "Париж - Франция - 2148271"
city3 = "Токио - Япония - 13969100"
city4 = "Нью-Йорк - США - 8537673"
city5 = "Лондон - Великобритания - 8825000"
def check_city(a):
    a = a.split(" - ")
    a.pop(2)
    if a[0][0] == "М" or a[0][0] == "м":
        a = " - ".join(a)
        a=a.upper()
        return a
    if len(a[0].split("-")) >= 2:
        a = " - ".join(a)
        a=a.lower()
        return a
check=check_city(city1)
print(check)
def print_city(a):
    a=a.split(" - ")
    b=". ".join(a)
    return b
print(print_city(city1))