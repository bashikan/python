#txt1
# x=[3,15,123]
# print(x[1])

#txt2
# x=["3","ABCabc",12345,[10,20,"ABC"],333]
# print(x[3][1])

#txt3
# x=[]

#txt4
# x=[]
# y=[225,13,50,1002,133,99]
# x+=y
# print(max(x),min(y))

#txt5
# x=[]
# y=[225,13,50,1002,133,99]
# x+=y
# nx=sorted(x)
# print(nx)

#txt6
# x=[]
# y=[225,13,50,1002,133,99]
# x+=y
# nx=sorted(x,reverse=True)
# print(nx)

#txt7
# x=[]
# y=[225,13,50,1002,133,99]
# x+=y
# print(x[3:6])

#txt8
# x=[]
# y=[225,13,50,1002,133,99]
# x+=y
# x[3:6]=[10,10,10]
# print(x)

#txt9
# x=[777,888,999]
# y=[225,13,50,1002,133,99]
# y+=x
# print(y)

#txt10
# x=[777,888,999]
# y=[225,13,50,1002,133,99]
# y+=x
# i=len(y)
# print(i)

#txt11
# x=[777,888,999]
# y=[225,13,50,1002,133,99]
# y+=x
# y.insert(7,117)
# print(y)

#txt12
# x=[777,888,999]
# y=[225,13,50,1002,133,99]
# y+=x
# y.insert(7,117)
# y.remove(117)
# print(y)

#txt13
# x=[777,888,999]
# y=[225,13,50,1002,133,99]
# y+=x
# y.insert(7,117)
# y.remove(117)
# del y[:]
# print(y)

#txt14
# x=[777,888,999]
# y=[225,13,50,1002,133,99]
# y+=x
# y.insert(7,117)
# y.remove(117)
# y.clear()
# print(y)

#txt15
# print('合計点と平均点を求めます')
# nin=int(input('学生の人数:'))
# ten=[None]*nin
# for i in range(nin):
#     ten[i]=int(input('{}番目の点数:'.format(i+1)))
# sum=0
# for i in range(nin):
#     sum+=ten[i]
# print('合計は{}点です。'.format(sum))
# print('平均は{}点です。'.format(sum/nin))

#txt16
# print('合計点と平均点を求めます')
# print(':注"Endで入力終了"')
# nin=0
# ten=[]
# while True:
#     suu=input('{}番目の点数:'.format(nin+1))
#     if suu=='End':
#         break
#     ten.append(int(suu))
#     nin+=1
# sum=sum(ten)
# print('合計は{}点です。'.format(sum))
# print('平均は{}点です。'.format(sum/nin))
