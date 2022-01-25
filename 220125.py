### 등비수열

# 등비수열 

inputN1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

valueN = 0

n=1
while n <= inputN:

  if n == 1:
    valueN = inputN1
    print(f'{n}번째 항의 값: {valueN}')
    n += 1
    continue

  valueN = valueN * inputR
  print(f'{n}번째 항의 값: {valueN}')
  n+=1


# 등비수열 일반항 개념 활용

inputN1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

# an = a1*r^(n-1)
valueN = inputN1 * (inputR ** (inputN - 1))
print(f'{inputN}번째 항의 값: {valueN}')


# 등비수열의 합
inputN1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

valueN = 0
sumN = 0
n = 1
while n <= inputN:
  if n == 1:
    valueN = inputN1
    sumN += valueN
    print(f'{n}번째 항까지의 합: {sumN}')
    n += 1
    continue

  valueN *= inputR
  sumN += valueN
  print(f'{n}번째 항까지의 합: {sumN}')
  n += 1

# 등비수열의 합 <- 공식이용
inputN1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

sumN = inputN1 * ( 1- (inputR ** inputN)) / (1-inputR)
print(f'{n}번째 항까지의 합: {sumN}')

# ### 시그마
# 수열의 합을 나타내는 기호  
# 일반항 = 2k <- 등차수열  
# 일반항 = # 2*3^(k-1) <- 등비수열


# sn = n(a1+an) / 2
# an = a1 + (n-1)d
inputN1 = int(input('a1 입력: '))
inputD = int(input('공차 입력: '))
inputN = int(input('n 입력: '))

valueN = inputN1 + (inputN-1)*inputD
sumN = inputN * (inputN1 + valueN) / 2
print(f'{inputN}번째 까지의 합: {sumN}')

# 등비수열
inputN1 = int(input('a1 입력: '))
inputR = int(input('공비 입력: '))
inputN = int(input('n 입력: '))

sumN = inputN1 * ( 1- (inputR ** inputN)) / (1-inputR)
print(f'{n}번째 항까지의 합: {sumN}')


# ### 계차수열
# - 두 항의 차로 이루어진 또 다른 수열
# - 계차 수열을 이용해서 수열 an의 일반항을 구할 수 있음
# - b1~bn-1 까지의 합 = an-a1

# an = {3,7,13,21,31,43,57}
# bn = {4, 6, 8, 10, 12, 14}

inputAN1 = int(input('a1 입력: '))
inputAN = int(input('an 입력: '))
inputBN1 = int(input('b1 입력: '))
inputBD = int(input('bn 공차 입력: '))

valueAN = 0
valueBN = 0

n = 1
while n <= inputAN:

  if n==1:
    valueAN = inputAN1
    valueBN = inputBN1
    print(f'an의 {n}번째 항의 값: {valueAN}')
    print(f'bn의 {n}번째 항의 값: {valueBN}')
    n += 1
    continue

  valueAN = valueAN + valueBN
  valueBN = valueBN + inputBD
  print(f'an의 {n}번째 항의 값: {valueAN}')
  print(f'bn의 {n}번째 항의 값: {valueBN}')
  n += 1

print(f'an의 {inputAN}번째 항의 값: {valueAN}')
print(f'bn의 {inputAN}번째 항의 값: {valueBN}')

# 공식 이용
valueAN = inputAN ** 2 + inputAN + 1
print(f'an의 {inputAN}번째 항의 값: {valueAN}')

# ### 피보나치 수열
# - 1쌍의 토끼가 n달 뒤 또다른 암수 1쌍을 낳음...
# - 1 1 2 3 5 8 13 21 ... 
# - 앞 두 단계를 합하면 그다음 값이 나옴
# - a1+a2 = a3
# - an = an-2 + an-1

# 파이썬으로 피보나치 수 계산하기
inputN = int(input('n 입력: '))
valueN = 0
sumN = 0

valuePreN2 = 0
valuePreN1 = 0

n= 1
while n <= inputN:
  if n ==1 or n ==2:
    valueN = 1
    valuePreN2 = valueN
    valuePreN1 = valuePreN1

    sumN += valueN
    n += 1
  else:
    valueN = valuePreN2 + valuePreN1
    valuePreN2 = valuePreN1
    valuePreN1 = valueN
    sumN += valueN
    n+=1
print(f'{inputN}번째 항의 값: {valueN}')
print(f'{inputN}번째 항까지의 합: {sumN}')


# ### 팩토리얼
# - 1부터 양의 정수 n까지의 정수를 모두 곱한 것

# 반복문 이용하는 경우
inputN = int(input('n 입력: '))

result = 1
for n in range(1, inputN+1):
  result *= n

print(f'{inputN}팩토리얼: {result}')

# 재귀함수를 이용하는 경우
inputN = int(input('n 입력: '))

def fac(n):
  if n==1:return 1
  return n*fac(n-1)
print(f'{inputN}팩토리얼 :{fac(inputN)}')

# math 모듈에 있는 factorial 기능 사용하는 방법
import math 


# ### 군수열
# - 여러 항을 묶었을 때 규칙성을 가지는 수열

inputN = int(input('n항 입력: '))

flag = True
n = 1; nCnt = 1; searchN = 0

while flag:
  for i in range(1, n+1):
    print(f'{i}', end="")
    # if i == n:
    #   print()
    # else:
    #   print()

    nCnt += 1
    if (nCnt > inputN):
      searchN = i
      flag = False
      break
  print()
  n+=1
print(f'{inputN} : {searchN}')

# ### 순열
# - n개에서 r개를 택해 나열하는 경우의 수 (여기부터 추가해야 함)