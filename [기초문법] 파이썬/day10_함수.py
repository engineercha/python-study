def getsum(x):
    sum=0
    for i in range(x+1):
        sum+=i
    return sum


num=int(input("정수를 입력하세요: "))
print(getsum(num))


#[함수, 반복문] 최대값 위치 출력하기
import random

def getmax_idx(x):
    max=0
    for i in range(1,len(x)):
        if x[i] > x[max]:
            max=i
    return max

    
numbers=[random.randrange(1,2021) for i in range(0,10)]
print(numbers,"중")
print("최대값은 %d"%getmax_idx(numbers)+"번째에 있습니다.",end='\n\n')

#ver2
import random
def getmax_idx(x):

    max_value=max(x)
    max_idx=[]

    for i in range(1,len(x)):
        if x[i]==max_value:
            max_idx.append(i)
    return max_idx

numbers=[random.randrange(1,10) for i in range(0,20)]
print(numbers)
print("max = %d = "%max(numbers),end='')
for i in getmax_idx(numbers):
    if i==getmax_idx(numbers)[-1]:    #마지막 인덱스는 , 출력하지 않음
        print("numbers[%d]"%i)
    else: print("numbers[%d]"%i,end=', ')