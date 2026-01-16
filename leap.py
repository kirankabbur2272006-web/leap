def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


if __name__ == "__main__":
    y = int(input("Enter a year: "))
    print(is_leap(y))
