import numpy as np
import pandas as pd

names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
class_name = ['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']
df = pd.read_csv('iris.data.txt', header=None, names=names)
E = 1.59
for name in names[:4]:
    print(name)
    df.sort_values(name)
    # print(df)
    mi = df[name].min()
    ma = df[name].max()

    length = (ma-mi)/3
    print('divide:')
    print([mi, mi +length, mi+2*length, ma])
    count = np.empty((3,3))
    percentage = np.empty((3,3))
    percentage_sum = np.empty(3)
    son_sum = np.empty(3)
    son_sum[0] = df[(df[name] >= mi) & (df[name] < mi + length)].count()[1]
    son_sum[1] = df[(df[name] >= mi + length) & (df[name] < mi + 2 * length)].count()[1]
    son_sum[2] = df[df[name] >= mi + 2 * length].count()[1]
    for i in range(3):
        percentage_sum[i] = son_sum[i]/150
    # print(df[df['class'] == 'setosa'])
    for i,c in enumerate(class_name):
        count[i][0] = df[(df[name] >= mi) & (df[name] < mi + length) & (df['class'] == c)].count()[1]
        percentage[i][0] = count[i][0] / son_sum[0]
        count[i][1] = df[(df[name] >= mi+length) & (df[name] < mi+2*length)& (df['class'] == c)].count()[1]
        percentage[i][1] = count[i][1] / son_sum[1]
        count[i][2] = df[(df[name] >= mi+2*length) & (df[name] <= ma)& (df['class'] == c)].count()[1]
        percentage[i][2] = count[i][2] / son_sum[2]
    print('count：')
    print(count)
    print('son_sum:')
    print(son_sum)
    print(percentage)
    e = np.empty(3)
    for i in range(3):
        for j in range(3):
            if percentage[j][i] != 0:
                e[i]-=percentage[j][i] * np.log2(percentage[j][i])
    avg_e = np.sum(e*percentage_sum)
    print('IG:')
    print(E-avg_e)
