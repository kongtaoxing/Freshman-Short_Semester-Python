import csv #导入CSV模块
from matplotlib import pyplot as plt #导入pyplot模块
import numpy as np  #导入numpy模块    
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model         #导入最小二乘模型
from scipy.interpolate import make_interp_spline as mis #导入平滑曲线模块

def pic_num(x,y):
    n=5
    '''
    绘制一次拟合图像
    '''
    #根据公式计算k
    k =(n*np.sum(x*y)-np.sum(x)*np.sum(y)) /\
       (n*np.sum(np.power(x,2)) - np.sum(x) * np.sum(x))   
    #根据公式计算b
    b = 13.2-3*k
    lin = k*x+ b      
    plt.xlim(0.0,6.0)
    plt.ylim(-10.0,60)
    plt.xlabel('x')
    plt.ylabel('y')
    x_s=np.linspace(x.min(),x.max(),300)       #平滑x

    '''
    绘制二次拟合图像
    '''
    poly_reg2=PolynomialFeatures(degree=2) #二次多项式
    X_ploy2 =poly_reg2.fit_transform(x[:, np.newaxis])
    lin_reg_=linear_model.LinearRegression()    
    lin_reg_.fit(X_ploy2,y)
    b2=lin_reg_.coef_[[1]]
    a2=lin_reg_.coef_[[2]]
    de=lin_reg_.intercept_+b2*x+a2*x*x
    de_s=mis(x,de)(x_s)#平滑y

    '''
    绘制三次拟合曲线
    '''
    poly_reg =PolynomialFeatures(degree=3) #三次多项式
    X_ploy =poly_reg.fit_transform(x[:, np.newaxis])
    lin_reg_2=linear_model.LinearRegression()
    lin_reg_2.fit(X_ploy,y)
    c3=lin_reg_2.coef_[[1]]
    b3=lin_reg_2.coef_[[2]]
    a3=lin_reg_2.coef_[[3]]
    tri=lin_reg_2.intercept_+c3*x+b3*x**2+a3*x**3 
    tri_s=mis(x,tri)(x_s)#平滑y
    
    '''
    开始绘图
    '''
    plt.title('Curve Fitting')
    plt.plot(x,lin,'k',c='b')    #画出拟合函数
    plt.plot(x, y, 'o',c='r')    #画出样本数据
    plt.plot(x_s,tri_s,'k',c='k')
    plt.plot(x_s, de_s,'k',c='g')
    plt.show()

fp=open('附件3.csv') #打开文件
static=csv.reader(fp) 
string=[]
x0=[]
y0=[]
for row in static:
    string.append(str(row))
for i in range(5):
    x0.append(int(string[i+1][2]))  #将x导入x0数组
    y0.append(int(string[i+1][9]))  #将y导入y0数组
for i in range(3,5):
    y0[i]=y0[i]*10+int(string[i+1][10])
xn=np.array(x0)
yn=np.array(y0)
print('csv文件中的内容是：x:{},y:{}'.format(x0,y0))
print('红点是csv文件中的数据，蓝色是一次拟合方程，\
绿色是二次拟合方程，黑色是三次拟合方程！')
pic_num(xn,yn)     #调用函数绘制拟合图像
