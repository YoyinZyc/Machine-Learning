import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


def algebraic(x, y, n, dof):

    parameter_l = list()

    l = list()
    for i,v in enumerate(x):
        y[i] += x[i]*x[i] + 0.1 * x[i]
    x_trains = []
    y_trains = []
    x_tests = []
    y_tests = []
    mse = np.zeros(dof)
    for i in range(8):
        x_tests.append(x[i])
        y_tests.append(y[i])
        if i == 0:
            x_trains.append(x[1:])
            y_trains.append(y[1:])
        elif i == 7:
            x_trains.append(x[:7])
            y_trains.append(y[:7])
        else:
            x_trains.append(np.append(x[:i],x[i+1:]))
            y_trains.append(np.append(x[:i],y[i+1:]))
    for i in range(8):
        error = 0
        for m in range(0,dof):
            # ys = np.zeros(10)
            # print(m)
            parameters = np.polyfit(x_trains[i],y_trains[i],m)

            parameter_l.append(parameters)
            # print(parameters)
            # i = m
            # print(parameters)
            ys = np.polyval(parameters,x_tests[i])
            mse[m] += (ys-y_tests[i])**2
            # print(ys)
            # y_p[m] = ys
            # mse[m] = np.mean((ys-y) ** 2)

        # print(mse[m])
    # print (mse)
    mse = mse / 8
    index = mse.argmin()
    print(index)
    print(min(mse))
    return np.polyfit(x,y,index)
    # p = np.zeros(dof)
    # for i in range(dof):
    #     p[i] = (i+1) / n
    # # print(p)
    # r = 1 + np.log(n) * p / (1-p)
    # # print(r)
    # # print('mse:')
    # # print(mse)
    # R = r * mse
    # # print('R')
    # # print(R)
    # index = R.argmin()
    # print(index)
    # # print(R[index])
    # # print(p)
    # plt1 = plt.plot(x,y,'s',label = 'original values')
    # xi = np.linspace(0,1,100)
    # yi = np.polyval(parameter_l[index],xi)
    # # print(parameter_l[index])
    # # print(y[index])
    # # plt2 = plt.plot(xi,yi, 'r',label='polyfit values')
    # # plt.xlabel('x')
    # # plt.ylabel('y')
    # # plt.legend(loc=4) #指定legend的位置右下角
    # # plt.title('polyfitting')
    # # plt.show()
    # return parameter_l[index], R[index]
# plt.savefig('test.png')
# plt.figure()
# plt.scatter(x,y,'red')
# plt.
# x = np.random.random(size=10)
# print(x)
# y = np.random.normal(0,0.5,10)
# print(y)
# algebraic(x,y, 10,9)



