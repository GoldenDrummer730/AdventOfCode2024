
def is_safe(num_1: int, num_2: int):
    return (abs(num_1 - num_2)) == 1 or (abs(num_1 - num_2)) == 2 or (abs(num_1 - num_2)) == 3



file_input:str = 'big'

safe_reports:int  = 0


with open(f'Day 2\\day2_{file_input}.txt', 'r') as input:
    for line in input:
        safe:bool = True
        up:bool = True
        down:bool = True
        curr_line = [int(x) for x in line.split()]
        
        # Part 1
        # for i in range(1, len(curr_line)):
        #     if not (curr_line[i] > curr_line[i-1]):
        #         up = False
        #         break
        
        # if not up:
        #     for i in range(1, len(curr_line)):
        #         if not (curr_line[i] < curr_line[i-1]):
        #             down = False
        #             break
        
        # for i in range(1, len(curr_line)):
        #     if not is_safe(curr_line[i - 1], curr_line[i]):
        #         safe = False
        #         break
        # if safe and (up or down):
        #     # print(curr_line)
        #     safe_reports += 1

        # Part 2
        unsafe_reports = []
        for i in range(1, len(curr_line)):
            if not (curr_line[i] > curr_line[i-1]):
                up = False
                break
        
        if not up:
            for i in range(1, len(curr_line)):
                if not (curr_line[i] < curr_line[i-1]):
                    down = False
                    break
        
        for i in range(1, len(curr_line)):
            if not is_safe(curr_line[i - 1], curr_line[i]):
                safe = False
                break
        if safe and (up or down):
            # print(curr_line)
            safe_reports += 1
        else:
            unsafe_reports.append(curr_line)

        for report in unsafe_reports:
            value = 0
            #print(report)
            for skip_index in range(0, len(report)):
                safe:bool = True
                up:bool = True
                down:bool = True
                value = report.pop(skip_index)
                for i in range(1, len(report)):
                    if not (report[i] > report[i-1]):
                        up = False
                        break

                if not up:
                    for i in range(1, len(report)):
                        if not (report[i] < report[i-1]):
                            down = False
                            break

                for i in range(1, len(report)):
                    if not is_safe(report[i - 1], report[i]):
                        safe = False
                        break
                
                if safe and (up or down):
                    # print(f' New Safe: {value}, {safe}, {up}, {down}')
                    safe_reports += 1
                    break
                # else:
                #     print(f' Not Safe: {value}, {safe}, {up}, {down}')
                report.insert(skip_index, value)



print(safe_reports)