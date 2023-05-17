# 1, 2 , 3,........100
# divisible by 3 - 'Fizz'
# divisible by 5 - 'Buzz'
# divisible by both 3 and 5 - 'fizz buzz'

for i in range(1, 101):
  print(i)

  if i % 3 == 0 and i % 5 == 0:
    print('fizz buzz')
  elif i % 3 == 0:
    print('fizz')
  elif i % 5 == 0:
    print('buzz')