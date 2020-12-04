class NotValidIPAddress(Exception):
    def __init__(self):
        super().__init__('IP의 각 옥텟은 255를 초과할 수 없습니다.')

class NotValidSubnetmask(Exception):
    def __init__(self):
        super().__init__('Subnetmask prefix는 30을 초과할 수 없습니다.')

class IpCalculator:
    def check_calcType(self, num):
        if num == 1:
            self.subnet_calc()
        elif num ==2:
            self.network_calc()

    def ipList_divide(self):
        try:
            ip_List=input()
            ip_address, subnet_mask = ip_List.split('/')
            ip_address = ip_address.split('.')
            for i in ip_address:
                if int(i) > 255:
                    raise NotValidIPAddress
            if int(subnet_mask) > 30:
                raise NotValidSubnetmask
        except ValueError:
            print('\nXXX.XXX.XXX.XXX/XX 형식으로 IP를 입력해주세요.')
        except NotValidIPAddress as e:
            print("\nIP 주소 에러.", e)
        except NotValidSubnetmask as e:
            print("\nSubnetmask prefix 에러.", e)

        else:
            return ip_address, int(subnet_mask)
    
    def subnet_calc(self):
        try:
            print('[서브네팅 계산] 네트워크 ID를 입력해주세요. ex) 192.168.0.0/24')
            ip_address, subnet_mask = self.ipList_divide()
            nid_List, sn_tmp = [], []
            class_cnt = subnet_mask//8
            network_cnt = 2**(subnet_mask%8)
            host_cnt = int(256 / network_cnt)
        except: 
            print("유효하지 않은 값입니다. 다시 실행해주세요.")
        else:
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
                print("\t\t{0:02d}번 : {1}.{2}.{3}.{4}/{5}".format(i+1, nid_List[i][0], nid_List[i][1], nid_List[i][2], nid_List[i][3], subnet_mask))

    def network_calc(self):
        try:
            print('[네트워크 계산] 특정 IP를 입력해주세요. ex) 172.16.53.5/19')
            ip_address, subnet_mask = self.ipList_divide()
            nid_List, bid_List, sn_tmp = [], [], []
            class_cnt = subnet_mask//8
            network_cnt=2**(subnet_mask%8)
            host_cnt = int(256 / network_cnt)
            total_host_cnt = (2**(32-subnet_mask))-2
        except: 
            print("유효하지 않은 값입니다. 다시 실행해주세요.")
        else:
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
                elif sn_tmp[-1] <= int(ip_address[class_cnt]):
                    nid_List[class_cnt] = sn_tmp[-1]
                    if class_cnt == 3:
                        bid_List[class_cnt] = 254
                    else:
                        for j in range(class_cnt,4):
                            bid_List[j] = 255 
                    break
                #중간 서브넷에 속할 때
                elif sn_tmp[i] <= int(ip_address[class_cnt]) < sn_tmp[i+1]:
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
KTW = IpCalculator()
while True:
    print("원하는 계산을 선택해주세요. (1번: 서브네팅 계산 | 2번: 네트워크 계산) ", end='')
    try: 
        num = int(input())
        if not(num == 1 or num == 2) :
            raise Exception('\n1이나 2 이외의 숫자는 입력할 수 없습니다.\n')
    except ValueError:
        print('\n입력 값은 1이나 2이여야 합니다.\n')
        continue
    except Exception as e:
        print(e)
        continue
    else:
        KTW.check_calcType(num)

    print('\n추가 실행 하시겠습니까? Y | N')
    choose_yn = input()
    if choose_yn.lower() == 'y':
        print('\n====추가 실행====\n')
        continue
    elif choose_yn.lower() != 'y':
        print('====종료====\n')
        break