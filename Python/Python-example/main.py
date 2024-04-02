# def is_even_number(number):
#     if number % 2:
#         result = False
#     else:
#         result = True
#     return result
#
# print(is_even_number(2))
# print(is_even_number(3))

# def first_name(*names):
#     for name in names:
#         print(name[1:])
#
# first_name('차범근', '박지성', '손흥민', '이강인')

# def name_value(**kwargs):
#     for key, value in kwargs.items():
#         print('{} : {}'.format(key, value))
#
# name_value(name="<강병관>", age="25", dept="engineering")
# name_value(name="<송수미>", age="24", dept="engineering")

def add_and_sub(a, b):
    return a+b, a-b

# result = add_and_sub(12, 7)

# print(result)
# tuple로 전달됬구나. tuple은 수정이 불가능하다.

# 나는 더하기 결과만 알고 싶은데 tuple처럼 다루면 된다.
# print(result[0])

# 이렇게해서 불편하다? 그러면 따로 변수를 할당해야한다. (하지만 이것은 코드도 지저분해진다. 그래서 여러개를 받을 수 있다)

add, sub = add_and_sub(12, 7)
print(add)
print(sub)

