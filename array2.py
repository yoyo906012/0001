#-*- coding: utf-8 -*-

#--------------------------------------#

print('a 1 a 2 a 3 a 4 ')
print('a 5 a 6 a 7 a 8 ')
print('a 9 a10 a11 a12 ')
print('a13 a14 a15 a16 ')


#--------------------------------------#

N=4
arrA=[[None]*N for row in range(N)]
arrA[0][0]=input("請輸入a1: ")
arrA[0][1]=input("請輸入a2: ")
arrA[0][2]=input("請輸入a3: ")
arrA[0][3]=input("請輸入a4: ")
arrA[1][0]=input("請輸入a5: ")
arrA[1][1]=input("請輸入a6: ")
arrA[1][2]=input("請輸入a7: ")
arrA[1][3]=input("請輸入a8: ")
arrA[2][0]=input("請輸入a9: ")
arrA[2][1]=input("請輸入a10: ")
arrA[2][2]=input("請輸入a11: ")
arrA[2][3]=input("請輸入a12: ")
arrA[3][0]=input("請輸入a13: ")
arrA[3][1]=input("請輸入a14: ")
arrA[3][2]=input("請輸入a15: ")
arrA[3][3]=input("請輸入a16: ")
#宣告四維陣列
arrB=[[None] *N for row in range(N)]

print('[原本]')
for i in range(4):
    for j in range(4):
        print('%s' %arrA[i][j],end='\t')
    print()

#--------------------------------------#
#開轉#

for i in range(4):
    for j in range(4):
        arrB[i][j]=arrA[j][i]

print('[轉移後矩陣內容為]')
for i in range(4):
    for j in range(4):
        print('%s' %arrB[i][j],end='\t')
    print()
