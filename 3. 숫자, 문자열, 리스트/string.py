word = 'Python'
print(word[0])  # character in position 0
print(word[0:3])  # character from position 0 to 3


# 변수에 새로운 값을 넣으면 그냥 바뀌어요.
word = "I am new string"

# split 이라는 내장함수로 한번 글자를 나누어 봤어요. 
print(word.split())
i = 1
for token in word.split() :
  print(str(i) + " " + token)
  i = i + 1