num = [10, 3 , 3, 5, 15, 45, 21, 0, 7]
for i in num:
  if i%3 ==0 and i%5 ==0 and i != 0:
    print ('FizzBuzz')
  elif i % 3 ==0:
    print ("Fizz")
  elif i % 5 == 0:
    print('Buzz')
  else:
    print (i)
    