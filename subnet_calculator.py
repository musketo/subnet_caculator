class IpCalculator:
    def __init__(self):
        pass
    
    def check_CalcType(self, num):
        if num == 1:
            self.subnet_Calc()
        elif num ==2:
            pass
            self.network_Calc()
        else:
            print('다시 입력해주세요.')
            num = int(input())
            return self.check_CalcType(num)

    def ipList_Divide(self, ip_List):
        ip_address, subnet_mask = ip_List.split('/')
        ip_address = ip_address.split('.')
        return ip_address, int(subnet_mask)
    
    def subnet_Calc(self):
        print('[서브네팅 계산] 네트워크 ID를 입력해주세요. ex) 192.168.0.0/24')
        ip_List=input()
        ip_address, subnet_mask = self.ipList_Divide(ip_List)
        nid_List, sn_tmp = [], []
        class_cnt = subnet_mask//8
        network_cnt = 2**(subnet_mask%8)
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
        print("\n\t네트워크 개수는 총 {}개 입니다.\n\t대표 네트워크 ID:".format(network_cnt))
        for i in range(network_cnt):
            for j in range(4):
                if j < class_cnt:
                    nid_List[i][j] = int(ip_address[j])
                elif j > class_cnt:
                    nid_List[i][j] = 0
                elif j == class_cnt:
                    nid_List[i][j] = sn_tmp[i]
                nid_List[i][j] = str(nid_List[i][j])
            print("\t{0:02d}번 : {1}.{2}.{3}.{4}/{5}".format(i+1, nid_List[i][0], nid_List[i][1], nid_List[i][2], nid_List[i][3], subnet_mask))

    def network_Calc(self):
        print('[네트워크 계산] 특정 IP를 입력해주세요. ex) 172.16.53.5/19')
        ip_List=input()
        ip_address, subnet_mask = self.ipList_Divide(ip_List)
        nid_List, bid_List, sn_tmp = [], [], []
        class_cnt = subnet_mask//8
        network_cnt=2**(subnet_mask%8)
        host_cnt = int(256 / network_cnt)
        total_host_cnt = (2**(32-subnet_mask))-2

        for i in range(4):
            if i < class_cnt:
                nid_List.append(ip_address[i])
                bid_List.append(ip_address[i])
            else: 
                nid_List.append(0)
                bid_List.append(0)
        #뒤에 네트워크 ID만 저장한 리스트
        for i in range(0,256,host_cnt):
            sn_tmp.append(i)
        
        #host부분의 nid와 bid 계산
        for i in range(len(sn_tmp)):
            #서브넷 개수가 1개일때
            if len(sn_tmp) == 1:
                nid_List[class_cnt] = 0
                if class_cnt == 3:
                    bid_List[class_cnt] = 254
                else:
                    for j in range(class_cnt,4):
                        bid_List[j] = 255       
            #마지막 서브넷에 속할 때
            elif sn_tmp[-1] <= int(ip_List[class_cnt]):
                nid_List[class_cnt] = sn_tmp[-1]
                if class_cnt == 3:
                    bid_List[class_cnt] = 254
                else:
                    for j in range(class_cnt,4):
                        bid_List[j] = 255 
                break
            #중간 서브넷에 속할 때
            elif sn_tmp[i] <= int(ip_List[class_cnt]) < sn_tmp[i+1]:
                nid_List[class_cnt] = sn_tmp[i]
                bid_List[class_cnt] = sn_tmp[i+1] -1
                if class_cnt != 3:
                    for j in range(class_cnt+1,4):
                        bid_List[j] = 255
                break
        print("""
        해당 IP의 네트워크는 {0}.{1}.{2}.{3}/{4} 입니다.
        네트워크 ID: {0}.{1}.{2}.{3}
        브로드캐스트 IP: {5}.{6}.{7}.{8}
        사용 가능한 IP 개수: {9}개
        """.format(nid_List[0], nid_List[1], nid_List[2], nid_List[3], subnet_mask, bid_List[0], bid_List[1], bid_List[2], bid_List[3], total_host_cnt))
        

print("서브네팅 계산기입니다.")
while True:
    KTW = IpCalculator()
    print("원하는 계산을 선택해주세요. (1번: 서브네팅 계산 | 2번: 네트워크 게산) ", end='')
    num = int(input())
    KTW.check_CalcType(num)
    
    print('\n추가 실행을 하시겠습니까? Y | N')
    choose_yn = input()
    if choose_yn.lower() == 'y':
        print('\n====추가 실행====\n')
        continue
    elif choose_yn.lower() == 'n':
        print('====종료====\n')
        break




