def network_calc (ip_List, sn):
    sn = int(sn)
    nid_List = []
    sn_tmp = []
    class_cnt = sn//8
    network_cnt=2**(sn%8)
    host_cnt = int(256 / network_cnt)

    #2차원 리스트 선언
    for i in range(0,network_cnt):
        tmp = []
        for j in range(4):
            tmp.append(j)
        nid_List.append(tmp)
    #뒤에 네트워크 ID만 저장한 리스트
    for i in range(0,256,host_cnt):
        sn_tmp.append(i)
    #2차원 리스트로 정렬
    print("\n대표 네트워크 ID: \n총 {0}개 입니다.\n".format(network_cnt))
    for i in range(network_cnt):
        for j in range(4):
            if j < class_cnt:
                nid_List[i][j] = int(ip_List[j])
            elif j > class_cnt:
                nid_List[i][j] = 0
            elif j == class_cnt:
                nid_List[i][j] = sn_tmp[i]
            nid_List[i][j] = str(nid_List[i][j])
        print('{0:02d}번 : {1}.{2}.{3}.{4}/{5}'.format(i+1, nid_List[i][0], nid_List[i][1], nid_List[i][2], nid_List[i][3], sn))


print("서브네팅 계산기입니다.")

while 1:
    # 원하는 계산 선택
    print("원하는 계산을 선택해주세요. (1번: 서브네팅 계산 | 2번: 네트워크 게산) ", end='')
    choose_num = int(input())
    if choose_num == 1:
        print('[서브네팅 계산] 네트워크 ID를 입력해주세요. ex) 192.168.0.0/24')
        ip_List, sn = input().split('/')
        ip_List = ip_List.split('.')
        network_calc(ip_List, sn)


    elif choose_num == 2:
        print('특정 IP의 네트워크 확인')
        # 네트워크 확인 함수 구현
    else: 
        print('다시 입력해주세요.')
        continue

    # 동작 이후 추가 실행 또는 종료 선택
    print('\n추가 실행을 하시겠습니까? Y | N')
    choose_yn = input()
    if choose_yn.lower() == 'y':
        print('\n====추가 실행====\n')
        continue
    elif choose_yn.lower() == 'n':
        print('====종료====\n')
        break




