def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                # print("Leap year.")
                return True
            else:
                # print("Not a leap year.")
                return False
        else:
            # print("Leap year.")
            return True
    else:
        print("Not a leap year.")

def days_in_month():
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30 31]
