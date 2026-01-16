import sys

def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        y = int(sys.argv[1])
        if is_leap(y):
            print(f"{y} is leap year.")
        else:
            print(f"{y} is not leap year.")
