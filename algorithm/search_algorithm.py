def binary_search(data, value):
    left = 0            # 探索する範囲の左端を設定
    right = len(data) - 1            # 探索する範囲の右端を設定
    while left <= right:
        mid = (left + right) // 2            # 探索する範囲の中央を計算
        if data[mid] == value:
            # 中央の値と一致した場合は位置を返す
            return mid
        elif data[mid] < value:
            # 中央の値より大きい場合は探索範囲の左を変える
            left = mid + 1
        else:
            # 中央の値より小さい場合は探索範囲の右を変える
            right = mid - 1
    return -1            # 見つからなかった場合

def bubble_sort():
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    change = True
    for i in range(len(data)):
        if not change:    # 交換が発生していなければ終了
            break
        change = False    # 交換が発生していないものとする
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                change = True    # 交換が発生した

def partition(num):
    l=[]
    l.append([num])
    for i in range(1,num):
        for j in partition(i):
            if j[0]<=num-i:
                l.append([(num-i)]+j)
    return l

def number_of_partition(num):
    l1=[]
    for i in range(1,num):
        l2=[]
        l2.append([i])
        for j in range (1,i):
            for k in (l1[j-1]):
                if k[0]<=i-j:
                    l2.append([(i-j)]+k)
        l1.append(l2)
    d1=[]
    for i in l1:
        d2=[]
        for k in i:
            prev=0
            for l in k:
                if prev==0:
                    prev=l
                else:
                    if prev==l:
                        break
                    else:
                        prev=l
            else:
                d2.append(k)
        d1.append(d2)
    return d1