#function is the block of code that performs specific task
tom_exp_list = [2100, 3400, 3500]
joe_exp_list = [200, 500, 700]

total = 0
for item in tom_exp_list:
    total = total + item
print("Tom's total expense:", total)

total = 0
for item in joe_exp_list:
    total = total + item
print("Joe's total expense:", total)