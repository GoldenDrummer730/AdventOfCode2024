import re


file_input:str = 'big'

sum = 0
on_off_flag = True

with open(f'Day 3\\day3_{file_input}.txt', 'r') as input:
    data = input.read(-1)

    # Part 1 regex: mul\\(\\d{1,}\\,\\d{1,}\\)
    # Part 2 regex: mul\\(\\d{1,}\\,\\d{1,}\\)|don\'t\\(\\)|do\\(\\)
    groups = re.findall('mul\\(\\d{1,}\\,\\d{1,}\\)|don\'t\\(\\)|do\\(\\)', string=data)
    
    for g in groups:
        if re.fullmatch('don\'t\\(\\)', g) is not None:
            on_off_flag = False
            continue
        elif re.fullmatch('do\\(\\)', g) is not None:
            on_off_flag = True
            continue
        elif on_off_flag:
            nums = re.findall(pattern='\\d{1,}', string=g)
            sum += int(nums[0]) * int(nums[1]) # We can hard code this given the problem statement telling us that mul will have 2 numbers in it

print(sum)