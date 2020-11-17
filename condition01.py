#입력을 받습니다.
number=input("정수 입력>")

#마지막 자리 숫자를 추출
last_character=number[-1]

#숫자로 변환하기
last_nmuber=int(last_character)

#짝수 확인
if last_nmuber==0\
    or last_nmuber==2\
    or last_nmuber==4\
    or last_nmuber==6\
    or last_nmuber==8:
    print("짝수입니다.")

#홀수 확인
if last_nmuber==1\
    or last_nmuber==3\
    or last_nmuber==5\
    or last_nmuber==7\
    or last_nmuber==9:
    print("홀수입니다")