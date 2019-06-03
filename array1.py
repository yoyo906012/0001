#input UTF-8
#-*- coding: utf-8 -*-

#行列式計算機
#決定陣列的維度
N = 2
arr = [[None]*N for row in range(N)]
print("|a1 b1|")
print("|a2 b2|")
#input 行列式
    arr[0][0] = input("請輸入a1: ")
    arr[0][1] = input("請輸入b1: ")
    arr[1][0] = input("請輸入a2: ")
    arr[1][1] = input("請輸入b2: ")
#求行列式的值
    result = ((int(arr[0][0])*int(arr[1][1]))-(int(arr[0][1]*int(arr[1][0]))))
        print('|%d %d|' %(int(arr[0][0]),int(arr[0][1])))
        print('|%d %d|' %(int(arr[1][0]),int(arr[1][1])))
        print("行列式的值＝ %d" %result)
