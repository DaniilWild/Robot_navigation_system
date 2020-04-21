from random import randint  , uniform
#from random import *


#points = [  [20,0,0.2] , [20,10,0.2] , [15,-10 ,0.15],[20 ,-10,0.2] , [15,0 ,0.15] ,  [10,-10,0.1], [10,10,0.1] , [20,18,1.7] ,[15,-15,1.2],[15,10 ,0.15] ]
def generator(col_good_points , col_bad_points ):
    

    if  col_bad_points >= col_good_points:
        print('Ошибка колличество точек пола должно первышать "шум" !!!')

    else:
        mas_points = []
        p = randint(1,50)/100

        A = round(uniform(-50,50), 2)
        B = round(uniform(-50,50), 2)
        C = round(uniform(-50,50), 2)
        D = round(uniform(-50,50), 2)

        max_num = max(abs(A) , abs(B) , abs(C) , abs(D))

        if max_num!=0:
            A /= max_num
            B /= max_num
            C /= max_num
            D /= max_num
   
        i=0
        while i< col_good_points: 
            x0 = round(uniform(-10,10), 2)
            y0 = round(uniform(-10,10), 2)
            z0 = (-A*x0-B*y0-D)/C #+ round(uniform(-p,p), 3)*((A**2+B**2+C**2)**(1/2))
            if abs(z0)<=100:
                arr = [x0 ,y0 , z0]
                mas_points.append(arr)
                i+=1
  
        i=0
        while i< col_bad_points:
            x0 = round(uniform(-100,100), 2)
            y0 = round(uniform(-100,100), 2)
            z0 = (-A*x0-B*y0-D)/C + round(uniform(p,3*p), 3)*((A**2+B**2+C**2)**(1/2))
            if abs(z0)<=100:
                arr = [x0 ,y0 , z0]
                mas_points.append(arr)
                i+=1

        abc = [A,B,C ,D]
        #print(mas_points)
        return mas_points , p , len(mas_points) , abc


