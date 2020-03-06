def solution(number):
  num = []
  for x in range(0, number, 3):
      num.append(x)
  for x in range(0, number, 5):
      if x % 3 != 0:
          num.append(x)
  return sum(num)
