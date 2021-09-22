#9-1
# def school_name(school,name):
#     print('学校名:',school)
#     print('名前:',name)

# school = '東京情報クリエイター工学院専門学校'
# name = '竹井一馬'

# school_name(school,name)

#9-2
# def Hello():
#     for i in range(10):
#         print('Hello')
# Hello()

#9-3
# def kotoba(moji,count):
#     for i in range(count):
#         print(moji)

# kotoba('Hello',3)
# kotoba('Good morning',4)
# kotoba('Good evening',2)


#9-4
# def bai(count):
#     a=count*3
#     return a

# count=int(input('整数を入力してください:'))
# sum=bai(count)
# sum2=bai(sum)
# print('{}の9倍は{}です。'.format(count,sum2))

#9-5
# def keisan(sei1,sei2):
#     tashi=sei1+sei2
#     print('{}+{}={}'.format(sei1,sei2,tashi))
#     hiki=sei1-sei2
#     print('{}-{}={}'.format(sei1,sei2,hiki))
#     kake=sei1*sei2
#     print('{}*{}={}'.format(sei1,sei2,kake))
#     wari=sei1//sei2
#     print('{}/{}={}'.format(sei1,sei2,wari))
#     ama=sei1%sei2
#     print('{}%{}={}'.format(sei1,sei2,ama))
# sei1=int(input('整数を入力してください:'))
# sei2=int(input('整数を入力してください:'))
# keisan(sei1,sei2)

#9-6
# def sumn(hairetu):
#     aa=sum(hairetu)
#     return aa
# hairetu=[4,10,59,679,1991,3994,6789,19324]
# a=sumn(hairetu)
# print(a)

#9-7
# def kakuni(a,hairetu):
#     if a==a in hairetu:
#         print('{}配列に含まれています。'.format(a))
#     else:
#         print('{}は配列に含まれていません。'.format(a))

# a=int(input('整数を入力してください:'))
# hairetu=[4,10,59,679,1991,3994,19324]
# kakuni(a,hairetu)

#9-8
# def renhai(array):
#     #キー配列の取得
#     keys=list(array.keys())
#     #要素分ループ
#     for key in keys:
#         value=array.get(key)
#         #値を表示
#         print(key,':',value,sep='')
# color={'赤':'red','白':'white','黒':'black','青':'blue','緑':'gureen'}
# renhai(color)

#9-9