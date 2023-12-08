# 함수
import random
def selectSort(ary):
    n = len(ary)   # 데이터 총 개수
    for i in range(0, n-1): # 사이클
        minIdex = i
        for k in range(i+1, n):
            if ary[minIdex] > ary[k]:
                minIdex = k
        ary[i], ary[minIdex] = ary[minIdex], ary[i]

    return ary

## 변수
dataAry = [random.randint(30, 190)for _ in range(8)]

## 메인
print('정렬 전-->', dataAry)
dataAry = selectSort(dataAry)



print('정렬 후-->', dataAry)