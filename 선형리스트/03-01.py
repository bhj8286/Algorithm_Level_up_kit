## 함수 선언부





## 전역 번수부
kakaotalk = ['다현', '정연', '쯔위', '사나', '지효']





## 메인 코드부
print(kakaotalk)

## ** 데이터 추가 : 모모가 메시지 1회 
# 1단계: 빈칸 추가
kakaotalk.append(None)
#2단계: 마지막 칸에 대입 
kakaotalk[5]='모모'
print(kakaotalk)


##  ** 데이터 삽입: 미나카 메시지 40회 --> 미나를 3등으로
# 1단계: 빈칸 추가
kakaotalk.append(None)
# 2단계: 한칸씩 뒤로 이동... (마지막부터 3등까지)
kakaotalk[6] = kakaotalk[5]
kakaotalk[5] = None
kakaotalk[5] = kakaotalk[4]
kakaotalk[4] = None
kakaotalk[4] = kakaotalk[3]
kakaotalk[3] = None
# 3단계: 빈칸에 대입
kakaotalk[3] = '미나'
print(kakaotalk)

## ** 데이터 삭제: 사나가 카톡 차단 --> 4등(사나) 삭제하기
# 1단계: 지우기
kakaotalk[4] = None
# 2단계: 한칸씩 앞으로 
kakaotalk[4] = kakaotalk[5]
kakaotalk[5] = None
kakaotalk[5] = kakaotalk[6]
kakaotalk[6] = None
# 3단계: 칸을 없애기
del(kakaotalk[6])
print(kakaotalk)
