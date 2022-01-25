# 기초수학1

# 약수 구하기
inputNumber = int(input("0보다 큰 정수 입력: "))
for number in range(1, inputNumber + 1):
  if inputNumber % number == 0:
    print(f'{inputNumber}의 약수: {number}')

# 소수와 합성수 판별기
inputNumber = int(input("0보다 큰 정수 입력: "))
for number in range(2, inputNumber+1): #1은 소수가 아니므로 2부터 시작
  flag=True
  for n in range(2, number):
    if number % n == 0:
      flag=False
      break
  if flag:
    print(f'{number}: 소수!!')
  else:
    print(f'{number}: \t\t합성수!!')

# 소인수 = 약수 중 소수인 수 
# 소인수 분해
inputNumber = int(input("보다 큰 정수 입력: "))

n=2
while n <= inputNumber:
  if inputNumber % n == 0:
    print(f"소인수: {n}")
    inputNumber /= n
  else:
    n += 1


inputNumber = int(input("보다 큰 정수 입력: "))

n=2
searchNumbers = []
while n <= inputNumber:
  if inputNumber % n == 0:
    print(f"소인수: {n}")
    if searchNumbers.count(n) == 0:
      searchNumbers.append(n)
    elif searchNumbers.count(n) == 1:
      searchNumbers.remove(n)
    inputNumber /= n
  else:
    n += 1
print(f'searchNumbers: {searchNumbers}')

# 공약수
num1 = int(input("1보다 큰 정수 입력 : "))
num2 = int(input("1보다 큰 정수 입력 : "))
 
for i in range(1, (num1+1)):
  if num1 % i == 0 and num2 % i == 0:
    print(f"공약수:{i}")
    maxNum=i
print(f"최대공약수: {maxNum}")

# 유클리드 호제법 = x,y의 최대공약수는 y,r(x%y)의 최대공약수와 같다
num1 = int(input("1보다 큰 정수 입력 : "))
num2 = int(input("1보다 큰 정수 입력 : "))

temp1=num1
temp2 = num2

while temp2 > 0:
  temp = temp2
  temp2 = temp1 % temp2
  temp1 = temp
print(f'{num1}, {num2}의 최대 공약수: {temp1}')

# 최소공배수 num1 < num2
num1 = int(input("1보다 큰 정수 입력 : "))
num2 = int(input("1보다 큰 정수 입력 : "))
maxNum=0

for i in range(1, (num1+1)):
  if num1 % i == 0 and num2 % i ==0:
    print(f'공약수: {i}')
    maxNum=i
print(f'최대공약수: {maxNum}')

minNum = (num1*num2) // maxNum
print(f'최소공배수: {minNum}')

# 세가지 수의 최소공배수는 두개의 수의 최소공배수를 먼저 구한 다음 구함


ship1 = 3
ship2 = 4
ship3 = 5
maxDay=0

for i in range(1, (ship1+1)):
  if ship1%i ==0 and ship2%i ==0:
    maxDay=i
print(f'최대공약수:{maxDay}')

minDay = (ship1*ship2) // maxDay
print(f'{ship1}, {ship2}의 최소공배수: {minDay}')

dNum=30
print('2진수:', type(bin(dNum)))
print('8진수:', oct(dNum))
print('16진수:', hex(dNum))

print(format(dNum, '#b'))
print(format(dNum, '#o'))
print(format(dNum, '#x'))

print('{0:#b}'.format(dNum))
print('{0:#o}'.format(dNum))
print('{0:#x}'.format(dNum))

## 하다가 맘 