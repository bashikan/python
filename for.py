#6-1
# for i in range(10):
#     print('for文のプログラムです')

#6-2
# sum=0
# for i in range(101):
#     sum+=i
# print('合計は{}です'.format(sum))

#6-3
# n=10
# for i in range(1,n+1):
#     print('{}'.format(i),end='')

#6-4
# n=10
# for i in range(1,n+1,2):
#     print('{}'.format(i),end='')

#6-5

#6-6
# start=int(input('開始数:'))
# end=int(input('終了数:'))
# sum=0
# for i in range(start,end):
#     sum+=i
# print('合計{}'.format(sum+end))

#九九の表
# print('-'*27)
# for i in range(1,10):
#     for j in range(1,10):
#         print('{:3d}'.format(i*j),end='')
#     print()
# print('-'*27)



#6-7
# n=1
# j=10
# for i in range(1,10):
#     print('{}の段'.format(i))
#     for j in range(1,10):
#         print('{}×{}={}'.format(i,j,i*j))

#6-11
# print('長方形を描画します')
# print('2~20までの整数値を入力してください')
# x=int(input('行数の入力:'))
# y=int(input('列数の入力:'))
# if x>20 or x<2:
#     print('値が正しくありません')
# elif y>20 or x<2:
#     print('値が正しくありません')
# else:
#     for i in range(x):
#         for j in range(y):
#             print('*',end='')
#         print()

#6-12
