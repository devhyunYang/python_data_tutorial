# number = int(input("숫자를 입력하세요"))

# if  number < 5:
#     print("숫자가 5보다 작습니다.")
# elif 5< number< 10:
#     print("숫자가 5보다 크고 10보다 작다")
# else:
#     print("10보다 큽니다.")

# QUIZ
# money = int(input("숫자를 입력하세요"))

# if money == 70000:
#     print("비행기를 탑니다.")
# elif money == 50000:
#     print("기차를 탑니다.")
# elif money == 30000:
#     print("버스를 탑니다.")
# else:
#     print("걸어갑니다.")

# else는 필수 조건이 아니기 때문에 else가 없고, 이외의 값을 넣어도 아무런 문제가 생기지 않는다.

# 비교연산자
# and 조건문이 둘 다 참일 경우, or 하나라도 참일 경우

# 반복문(for)
# i(변수) in range(범위)
# print(range(10)) # rang(0,10) 0 <= x < 10 0~9

# for i in range(10):
#     print("hello world")

# for i in [1,2,3,4,5]:
#     print(i)

# countries = ["KO", "CH", "USA"]
# for country in countries: 만약 "countries" 문자열로 바꾸면 알파벳 하나하나 나옴
#     print(country)

# a = 0

# while a < 5: # True일 경우 부가적인 조건이 없다면 무한반복
#     a += 1 # a = a+1
#     print(a)

# QUIZ

# (1)
# result = 0
# for i in range(1,6):    
#     result = result + i # result += i
#     print(result)

# 제어문
for i in range(10): # 0~9
    if 3 <= i <=5:
        # continue # 반복문 코드의 처음으로 돌아간다.
        break # 반복문이 멈춘다.
    # print(i) # 0, 1, 2, 6, 7 , 8, 9
    print(i) # 0, 1, 2