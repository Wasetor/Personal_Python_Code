def computepay(hours, rate):
    if hours > 40:
        pay = (hours - 40) * .5 * rate + hours * rate
    else:
        pay = hours * rate

    return pay


hours = float(input("please input number of hours worked: "))
rate = float(input("input pay for each hour worked: "))

xp = computepay(hours, rate)
print("pay", xp)


def get_even_numbers(numbers):
    even_nums = [num for num in numbers if not num % 2]
    return even_nums


get_even_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


