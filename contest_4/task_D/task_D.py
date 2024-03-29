def check_middle(max_length, max_width, report):
    if max_width < max(report):
        return False

    length = 1
    cnt = 0
    while length <= max_length:
        width = max_width - report[cnt]
        cnt += 1
        while cnt <= len(report) - 1:
            if report[cnt] + 1 <= width:
                width -= report[cnt] + 1
                cnt += 1
            else:
                length += 1
                break

        if cnt == len(report):
            return True

    return False


def check_length(length, roll_width, report_1, report_2):
    left, right = max(report_1), roll_width
    while left < right:
        middle = (left + right) // 2
        if check_middle(length, middle, report_1):
            right = middle
        else:
            left = middle + 1

    if check_middle(length, roll_width - left, report_2):
        return True

    return False


roll_width, num_words_report_1, num_words_report_2 = map(int, input().split())
report_1 = list(map(int, input().split()))
report_2 = list(map(int, input().split()))

left, right = 0, max(num_words_report_1, num_words_report_2)
while left < right:
    length = (left + right) // 2
    if check_length(length, roll_width, report_1, report_2):
        right = length
    else:
        left = length + 1

result_length = left
print(result_length)
