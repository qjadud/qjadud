import math

a, b = map(int, input().split())  #첫번째 분자, 분모
A, B = map(int, input().split())  #두번째 분자, 분모
##입력받는 수가 한개이므로 map()함수를 써서 두 분수를 한번에 입력받음
numerator = (a*B) + (A*b) #분자
denominator = b * B       #분모
##통분

n = math.gcd(numerator, denominator)
##gcd()함수를 사용하여 분자와 분모의 최대공약수를 구함
numerator //= n
denominator //= n
##기약분수 만들기(약분하기)

print(numerator, denominator)
