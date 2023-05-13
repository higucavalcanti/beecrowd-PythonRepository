# 1068 - Balanço de Parênteses I

while True:
   try:
      caso = input()
      n = 0
      for i in range(len(caso)):
         if caso[i] == '(':
            n += 1
         elif caso[i] == ')':
            n -= 1
         if n < 0:
            break
      if n != 0:
         print('incorrect')
      elif n == 0:
         print('correct')
   except EOFError:
      break