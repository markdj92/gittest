'''N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.'''
#이분 탐색 재귀함수사용
n = int(input())
n_list=list(map(int, input().split()))

m=int(input())
m_list=list(map(int, input().split()))

n_list.sort() #이분탐색을 하기 위해서는 반드시 정렬을 해줘야 한다.

def binary_search(array, target, start, end):
    #정렬을 하고 타겟값을 정하고 시작값 끝값을 정해준다.
    if start > end:
        return 0 #시작 값이 끝 값보다 크다면 탐색이 끝난 것이므로 0값을 반환해준다.
    
    mid = (start+end) // 2 #처음 입력하는 리스트의 중앙 값을 설정해준다.

    if array[mid] == target:
        return 1
    #중앙부터 탐색을 시작한다. 탐색을 하면서 타겟값과 중앙값이 동일하다면 1을반환
    if array[mid] > target:
        return binary_search(array, target, start, mid-1)
    #만약 중앙 값이 타겟보다 크다면 중앙 값을 줄여나가면서 타겟을 탐색한다.
    if array[mid] < target:
    #만양 중앙 값이 타겟보다 작다면 중앙 값을 늘려나가면서 타겟을 탐색한다.     
        return binary_search(array, target, mid+1, end)
    
for i in m_list:
    #리스트안에 존재를 확인하며 1의 값을 반환하도록, 없다면 0을 반환하도록 설정한다.
    #리스트이 끝은 n-1로 설정해야 끝값을 프린트 할 수 있다
    print(binary_search(n_list, i, 0, n-1))


#반복문을 통한 이분 탐색
N = int(input())
N_li = list(map(int, input().split()))
M = int(input())
M_li = list(map(int, input().split()))

N_li.sort()

def binary_search(array, target, start, end):
    while start <= end: #시작값이 엔드값보다 작거나 같아 질때까지 반복하도록 설정한다.
        mid = (start + end)//2 #미드 값을 설정한다.

        if array[mid] == target:
            #만약 배열안에 미드값이 타겟값과 같다면 1을 가져온다.
            return 1
        elif array[mid] > target:
            #만약 미드값이 타겟 값보다 크다면 끝부분부터 미드값을 줄여나가면서 탐색한다.
            end = mid-1
        elif array[mid] < target:  # else문으로 대체 가능
            #만약 미드값이 타겟 값보다 작다면 처음부분부터 미드값을 늘려나가면서 탐색한다.
            start = mid+1
    return 0 # 탐색이 끝나면 종료한다.

for i in M_li:
    #리스트 안에 들어있는 엔드 값은 n-1번째 값이므로 잊지말고 설정해주도록한다.
    print(binary_search(N_li, i, 0, N-1))  
