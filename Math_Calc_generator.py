import random

repeat_qty=int(input('今天你想做几道题:'))
result=[]

for i in range(repeat_qty):
    first_no=random.randint(3,9)
    second_no=random.randint(6, 9)
    third_no=random.randint(3,17)
    mode=["+","-"]
    calc_mode=random.choice(mode)
    if calc_mode=="+":
        print(f"{first_no}*{second_no}{calc_mode}{third_no}=")
        result.append(first_no*second_no+third_no)
    else:
        print(f"{first_no}*{second_no}{calc_mode}{third_no}=")
        result.append(first_no*second_no-third_no)

input("请按回车键核对答案...")
for i in range(len(result)):
    if i<10:
        print("(", i+1,")",' ',8*".",result[i])
    else:
        print("(", i+1,")",8*".",result[i])
