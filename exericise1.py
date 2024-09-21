# start

positive_numbers: int = 0
negative_numbers: int = 0
count_even: int = 0
division_7: int = 0

for i in range(10):
    number = int(input('enter grade: '))
    if number == -999:
        break
    else:
        if not -9999:
            print(f"positive_numbers{positive_numbers}", f"negative_numbers{negative_numbers}")
            print(f"division_7{division_7}", f"number_0{number}")
    if positive_numbers is None or number > positive_numbers:
        max_number = number
    if negative_numbers is None or number < negative_numbers:
        min_number = number

    if number < -1000 or number > 1000:
        continue

    number += 1
positive_numbers += 0

count_even: int = positive_numbers // 7
print(f"total of {number}, average = {count_even:.2f}")

#end