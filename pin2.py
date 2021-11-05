
import time
t = 5
i = 0
while i>=0:
         print('enter PIN ')
         first = int(input())
         second = int(input())
         third = int(input())
         fourth = int(input())
         list = [first,second,third,fourth]
         pin= [0,0,0,0]
         if list == pin:
            print('correct PIN ')
         else:
            print('incorrect PIN ')
            i+=1
         if i>= 3 :
            print("wait ",t,"s")
            time.sleep(t)
            t = t+5



