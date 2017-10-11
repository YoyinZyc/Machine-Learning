from numpy import array, sort, absolute, tile, append
def knn(test, train, train_lable, k):
    dataset_size = train.shape
    distance = absolute(tile(test, dataset_size) - train)
    d = dict()
    for i, v in enumerate(distance):
        d[v] = train_lable[i]
    # a = array([2,1])
    # a.sort()
    # print(a)
    distance.sort()
    # print(distance)
    is_R = 0
    for v in distance[:k]:
        if d[v] == 'R':
            is_R+=1
        else:
            is_R-=1
    if is_R>0:
        return 'R'
    else:
        return 'D'
def validation(train, train_label, k):
    count = 0
    for i,v in enumerate(train):
        if i == 0:
            res = knn(v, train[1:],train_label[1:],k)
        elif i == 50:
            res = knn(v, train[:50],train_label[:50],k)
        else:

            res = knn(v, append(train[:i],train[i+1:]), append(train_label[:i],train_label[i+1:]),k)
        if res != train_label[i]:
            count+=1
    return count/51
if __name__ == '__main__':
    x = array([30.1,27.3,23.3,28.1,23.1,21.0,20.8,22.1,25.9,23.3,27.5,20.7,24.6,25.3,27.5,26.3,25.8,28.4,29.5,23.7,25.2,20.9,27.7,24.8,34.4,27.4,21.7,26.5,23.6,23.6,22.9,23.3,23.5,27.1,25.9,26.9,28.1,25.0,25.7,21.4,29.2,26.1,29.0,27.2,21.8,21.1,25.2,24.5,30.6,25.5,24.0,])
    y = array(['R','R','R','R','D','R','D','D','D','R','R','D','R','D','R','R','R','R','R','D','D','D','D','D','R','R','R','R','R','R','D','R','D','R','R','R','R','D','D','D','R','R','R','R','R','D','R','D','R','D','R'])
    for v in x:
        print (str(v) + knn(v,x,y,7))

    # print(x[:1])
    # k = array([3,5,7,9,11,13])
    # for v in k:
    #     print(validation(x,y,v))