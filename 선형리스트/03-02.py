## 함수 선언부
def add_data(friend):
    # 1단계: 빈칸 추카
    kakaotalk.append(None)
    KL = len(kakaotalk)
    # 2단계: 마지막 칸에 대입 
    kakaotalk[KL-1] = friend

def insert_data(position, friend):
    # 1단계: 빈칸 추가
    kakaotalk.append(None)
    KL = len(kakaotalk)
    # 2단계: 한칸씩 뒤로 이동 (반복)
    for i in range(KL-1, position, -1): 
        kakaotalk[i] = kakaotalk[i-1] 
        kakaotalk[i-1] = None
    # 3단계: 빈칸에 대입
    kakaotalk[position] = friend

def delete_data(position): 
    # 1단계: 지우기
    kakaotalk[position] = None
    KL = len(kakaotalk)
    # 2단계: 한칸씩 앞으로 이동
    for i in range(position+1, KL, 1):
        kakaotalk[i-1] = kakaotalk[i]
        kakaotalk[i] = None
    # 3단계: 마지막 칸 자체를 제거
    del(kakaotalk[KL-1])
   
## 전역 번수부
kakaotalk = []

## 메인 코드부
add_data('다현')
add_data('정연')
add_data('쯔위')
add_data('사나')
add_data('지효')
print(kakaotalk)

add_data('모모')
print(kakaotalk)

insert_data(3, '미나')
print(kakaotalk)

delete_data(4)
print(kakaotalk)
