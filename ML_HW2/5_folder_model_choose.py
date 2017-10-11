import numpy as np
import matplotlib.pyplot as plt
from model_choose import algebraic
def fit_error(train_x, val_x, train_y, val_y):

    ret = algebraic(train_x,train_y,8, 7)
    ys = np.polyval(ret, val_x)
    return np.mean((ys-val_y) ** 2)

# x = np.random.random(size=10)
x = np.array([ 0.39583024,0.97979459, 0.88204584, 0.12011592,0.88887401, 0.55750099, 0.06483857, 0.2924832, 0.93340658, 0.50538952])
# print(x)
# y = np.random.normal(0,0.5,10)
y = np.array([0.53604034, -0.04979956, 0.2046779, -0.1025203, -0.92141378, -0.5427099, -0.66146752, 0.28014246,0.15676682, -0.01386958])
    # ys = np.zeros(10)

    # print(ys)
    # y_p[m] = ys
errors = np.zeros(5)
# print(x[2:])
errors[0] = fit_error(x[2:], x[:2], y[2:], y[:2])
errors[1] = fit_error(np.append(x[:2],x[4:]), x[2:4], np.append(y[:2],y[4:]),y[2:4])
errors[2] = fit_error(np.append(x[:4],x[6:]), x[4:6], np.append(y[:4],y[6:]), y[4:6])
errors[3] = fit_error(np.append(x[:6],x[8:]), x[6:8], np.append(y[:6],y[8:]), y[6:8])
errors[4] = fit_error(x[:8], x[8:], y[:8], y[8:])
print(np.mean(errors))
# print('errors:')
# for i in range(5):
#     for j in range(2):
#         print(errors[i][j])
#
# # print(errors)
# print('mean:')
# mean = np.mean(errors, axis=0)
# print(mean[0])
# print(mean[1])
#     print(mse[m])
# print (mse)

# plt.savefig('test.png')
# plt.figure()
# plt.scatter(x,y,'red')
# plt.





