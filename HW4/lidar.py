from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
from valid_test import *

def plane_function(a,b,c):  # Функция построения плоскости через 3 точки
    mas =[]
    mas.append(a)
    mas.append(b)
    mas.append(c)

    x = (mas[1][1]-mas[0][1])*(mas[2][2]-mas[0][2]) - (mas[1][2]-mas[0][2])*(mas[2][1]-mas[0][1])
    y = (mas[1][0]-mas[0][0])*(mas[2][2]-mas[0][2]) - (mas[2][0]-mas[0][0])*(mas[1][2]-mas[0][2])
    z = (mas[1][0]-mas[0][0])*(mas[2][1]-mas[0][1]) - (mas[2][0]-mas[0][0])*(mas[1][1]-mas[0][1])
    D = -mas[0][0]*x -mas[0][1]*y - mas[0][2]*z

    max_num = max(abs(x) , abs(y) , abs(z) , abs(D))
        
    if max_num!=0:
        x /= max_num
        y /= max_num
        z /= max_num
        D /= max_num
    return x,y,z,D

def f (x, y):           #Задаем уравнение плоскости для отрисовки
    global x0 , y0 ,D0
    z = -x0*x -y0*y -D0
    return z
'''
p = float(input())
string_count = int(input())

points = []
for i in range(string_count):
    point = list(map(float , input().split()))
    points.append(point)
'''
points , p , string_count , abc = generator(3 ,0)

#print(points)
#string_count = 10
#points = [  [20,0,0.2] , [20,10,0.2] , [15,-10 ,0.15],[20 ,-10,0.2] , [15,0 ,0.15] ,  [10,-10,0.1], [10,10,0.1] , [20,18,1.7] ,[15,-15,1.2],[15,10 ,0.15] ]
#points = [ [20,0,3], [10,-10,2], [10,10,2] ]
#points = [ [20,0,0], [10,-10,0], [10,10,0] ]1
#p =0.01
#'''
j0=0
point_area_last = -1
stop = False

while j0 < string_count -2 and not stop: #пробегаемся по первой точке
    j1 = j0 + 1
    while j1 < string_count-1 and not stop: #пробегаемся по второй точке
        j2 = j1 + 1
        while j2 < string_count and not stop: #пробегаемся по третьей точке

            x , y ,z ,D = plane_function(points[j0], points[j1], points[j2])
            point_area =0
            for i in range(string_count):
                if x!=0 or y!=0 or z!=0:  # Такой плоскости не сушествует!
                    R = (x*points[i][0]+ y*points[i][1] + z*points[i][2]+D)/ ((x**2+y**2+z**2)**(1/2))
                    if abs(R)<= p:
                        point_area +=1

            if point_area > point_area_last:  # Если попало больше точек то перезапишем значения уравнения
                point_area_last = point_area
                x0 = x
                y0 = y
                z0 = z
                D0 = D
                print('{:.6f}'.format(x0),'{:.6f}'.format(y0), '{:.6f}'.format(z0), '{:.6f}'.format(D0))
            if point_area == string_count:
                stop = True
            j2+=1
        j1+=1
    j0+=1


if x0 >0 and (y0<0 or z0<0 or D0<0): #  Если есть возможность X должен быть отрицательным
    x0 /= -1
    y0 /= -1
    z0 /= -1
    D0 /= -1

print(abc)
print('{:.6f}'.format(x0),'{:.6f}'.format(y0), '{:.6f}'.format(z0), '{:.6f}'.format(D0))
points = np.array(points)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(points[:,0], points[:,1], points[:,2],c = 'red')   #Наносим все точки какие есть


xval = np.linspace(-20, 20, 100)
yval = np.linspace(-20, 20, 100)
x, y = np.meshgrid(xval, yval)
z = f(x, y)
surf = ax.plot_surface( x, y, z )    # Рисуем плоскость
plt.show()
