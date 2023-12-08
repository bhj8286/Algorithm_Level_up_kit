factValue = 1
for n in range(10,0,-1):
    factValue *= n
print('10*9*8*....*1 = ', factValue)

# 재귀식
def factorial(num):
    if num <= 1:
        return 1
    return num * factorial(num-1)

print('\n10! = ', factorial(10))

# 로케 발사
def countDown(n):
    if n == 0:
        print('발사!!')
    else:
        print(n)
        countDown(n-1)

countDown(5)

# 별 출력
def printStar(n):
    if n > 0:
        printStar(n-1)
        print('*'*n)

printStar(5)

# 구구단 
def gugu(dan, num):
    print('%d x %d = %d' % (dan, num, dan*num))
    if num < 9:
        gugu(dan, num+1)

for dan in range(2, 10):
    print('##%d단 ##' % dan)
    gugu(dan, 1)