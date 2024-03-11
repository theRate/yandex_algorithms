def is_leap_year(input_year):
    return True if input_year % 400 == 0 or (input_year % 4 == 0 and input_year % 100 != 0) else False


def calculate_day_of_week(input_number, input_month, input_start_day):
    month_number = months_of_year.index(input_month)
    amount_of_days = sum(days_per_month[:month_number]) + input_number
    day_number = amount_of_days % 7
    day_index = days_of_week.index(input_start_day) + day_number - 1
    if day_index > 6:
        result = days_of_week[day_index - 7]
    else:
        result = days_of_week[day_index]

    return result


number_of_holidays = int(input())  # количество государственных праздников
year = int(input())  # год
list_of_holidays = []  # список государственных праздников
for _ in range(number_of_holidays):
    list_of_holidays.append(input().split())
start_day = input()  # день недели 1-го января

days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if is_leap_year(year):
    days_per_month[1] += 1
days_of_week = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
months_of_year = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
                  'November', 'December')

count_days = {
    'Monday': 52,
    'Tuesday': 52,
    'Wednesday': 52,
    'Thursday': 52,
    'Friday': 52,
    'Saturday': 52,
    'Sunday': 52
}

if not is_leap_year(year):
    count_days[start_day] += 1
else:
    count_days[start_day] += 1
    index = days_of_week.index(start_day)
    if index == 6:
        count_days[days_of_week[0]] += 1
    else:
        count_days[days_of_week[index + 1]] += 1

for i in list_of_holidays:
    day = calculate_day_of_week(int(i[0]), i[1], start_day)
    count_days[day] -= 1

max_value = float('-inf')
min_value = float('inf')
max_key = ''
min_key = ''

for key, value in count_days.items():
    if value > max_value:
        max_value = value
        max_key = key
    if value < min_value:
        min_value = value
        min_key = key

print(max_key, min_key)
