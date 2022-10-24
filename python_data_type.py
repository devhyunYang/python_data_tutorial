x = "python" #문자형 str
x = 123 #int
x = "123" #str
x = [1, 2, 3, 4] #list
x = {"name" : "leo", "age" : 32} #dict
x = True #bool 앞 대문자

# print(type(x))
# 주석처리 : control + / 

a = 1 + 1
a = "1" + "1"
a = 100 - 1
a = 2 * 12
a = 3 / 4
# print(a)

# 여러 줄 나타내고 싶을 때 
# 1) \n 사용
a = "Act as though \nit is impossible to fail"
# print(a)

# 2) """ or ''' 사용 - 입력한 문자 형식 그대로 나옴
a = """Act as though 
it is impossible to fail
"""

# QUIZ
a = '"Failure is imply the opportunity to begin again." he says."'
a = """ "Failure is imply the opportunity to begin again." he says." """
a = "\"Failure is imply the opportunity to begin again.\" he says.\""
# print(a)

# 데이터 원본을 알아야 구조를 파악할 수 있음.

a = "A"
b = "B"
# print(a*b) 오류 문자열끼리 뺄셈, 곱셈 안됨.
# print(a*100) #a가 100번 나옴

c = "hello python!"
# print(len(c)) # 글자수 len()
print(c[0]) # indexing : 하나를 지정 첫번째 자리 글자
print(c[0:5]) # slicing : 범위를 지정 0 <= c < 5
print(c[6:]) # 끝까지 가져오고 싶을때 
print(c[:]) # 처음부터 끝까지

# Quiz2
x = "TitanicJames"
title = x[0:7]
director = x[7:]

# List : 대괄호
# a = ["a", "b", "c", "d", "e"]
a = ["a", "b", ["c", "d", "e"]]
# print(a[2][1])

# Tuple : 소괄호
t = ("a", "a", "a", "b")
# print(t)

# Dict
x = {"key1":"value1", "key2":"value2"}
# print(x["key2"]) # 원하는 키 값을 넣으면 value 값이 나옴

# Set : 순서를 갖지 않는다. 중복 허용하지 않는다.
x = set([5,2,2,1])
print(type(x)) 
print(x) # {1, 2, 5}

# Bool = True, False
