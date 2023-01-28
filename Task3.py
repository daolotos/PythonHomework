# Подсчет суммы знаков числа
def Sum(num):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
    return sum


ticketId = int(input("6ти значный номер билета:"))
if Sum(ticketId // 1000) == Sum(ticketId % 1000):
    print("Да")
else:
    print("Нет")
