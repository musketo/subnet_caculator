
print("서브네팅 계산기입니다.")

while 1:
    # 원하는 계산 선택
    print("원하는 계산을 선택해주세요. (1번: 서브네팅 계산 | 2번: 네트워크 게산) ", end='')
    choose_num = int(input())
    if choose_num == 1:
        print('서브네팅 계산을 선택하였습니다.')
        # 서브네팅 함수 구현
    elif choose_num == 2:
        print('특정 IP의 네트워크 확인')
        # 네트워크 확인 함수 구현
    else: 
        print('다시 입력해주세요.')
        continue

    # 동작 이후 추가 실행 또는 종료 선택
    print('추가 실행을 하시겠습니까? Y | N')
    choose_yn = input()
    if choose_yn.lower() == 'y':
        print('\n====추가 실행====\n')
        continue
    elif choose_yn.lower() == 'n':
        print('====종료====\n')
        break




