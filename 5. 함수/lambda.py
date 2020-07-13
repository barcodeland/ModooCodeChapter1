# 람다라는 함수가 있는데 당장 이해하실 필요는 없습니다. 
# 함수를 아주 간단하게 표현할때 쓰는데요. 언젠가 필요할 때 쓰시면 됩니다. 
# 어려우면 안써도 지장없습니다. 


# 먼저 lambda가 아닌 함수를 만들어볼게요. 
# 아래와 같이 x를 주면 1을 더해서 돌려주는 함수를 보세요. 
def addOne(x) : 
  return x + 1

# 1을 x로 함수에 전달하니 f(x) = x + 1에서 1 + 1 = 2가 됩니다. 
print(addOne(1))

# 그런데 아래처럼 한줄로 간단하게 표현할 수 있어요. 
addOneLambda = (lambda x : x + 1)

# 이것도 1 + 1이니 2로 동일합니다. 
print(addOneLambda(1))


# 왜 쓰냐하면 가끔 함수를 한번쓰고 버리거나 할 때 사용합니다. 
# 아래와 같이 1,2,3,4 가 들어있는 리스트(목록)이 있고 이 값들을 모두 제곱하고 싶습니다. 
numbers = [0,1,2,3,4]

# 람다를 안쓰면 함수 정의하고 호출하는데 3줄
def square(x) : 
  return x * x # 코딩에서 곱하기는 *입니당

# map이라는 것은 저런 목록을 돌면서 하나씩 처리해주는 함수예요.
# map 함수는 리스트에서 원소를 하나씩 꺼내서 함수를 적용시킨 결과를 새로운 # 리스트에 담아주니까, 위의 예제는 0을 제곱하고, 1을 제곱하고, 2, 3, 4를 # 제곱한 것을 새로운 리스트에 넣어주는 것입니다. 
square_result = list(map(square, numbers))
print(square_result)


# 람다를 쓰면 한줄로 되죠.


lambda_square_result = list(map(lambda x: x * x, numbers))
print(lambda_square_result)