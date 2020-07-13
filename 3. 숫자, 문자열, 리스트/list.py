squares = [1, 4, 9, 16, 25]

# squares에는 1, 4, 9, 16, 25가 들어있어요. 

squares.append(2)

print(squares)
# [1, 4, 9, 16, 25, 2] 가 출력됩니다. 

# 2가 맨 뒤에 있어서 마음에 안들어요. 

squares.sort()
print(squares)

# 아니 거꾸로요. 

squares.reverse()
print(squares)


# 3번째에 있는 거를 가져오고 싶어요. 
# 코딩에서 1번째는 항상 0부터 시작합니다. 
# 그래서 3번째는 0,1,2 2에 있는 거예요 

print(squares[2])