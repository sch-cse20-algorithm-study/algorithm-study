'''
책 10권의 총 가격과 가격을 읽을 수 있는 9권 가격이 주어졌을 때, 가격을 읽을 수 없는 책의 가격을 구하는 프로그램을 작성하시오.

입력 :첫째 줄에 10권의 총 가격이 주어진다. 둘째 줄부터 9개 줄에는 가격을 읽을 수 있는 책 9권의 가격이 주어진다. 책의 가격은 10,000이하인 양의 정수이다.
출력 : 첫째 줄에 가격을 읽을 수 없는 책의 가격을 출력한다.
'''

# 10개에 대한 리스트
# 첫번째 가격에서 다음 수들에 대한 뺄셈 -> 마지막으로 남은 수를 출력하기

total_fee = int(input()) # 첫째줄에 10권의 총 가격

for _ in range(9): # 책 9권에 대한 가격
    fee=int(input())
    total_fee -= fee # 총 가격에서 각 책의 가격을 계속하여 뺌
    
print(total_fee) # 마지막 한 권에 대한 요금 출력