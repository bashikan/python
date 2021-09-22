#1-1
# my_hensu=12345
# if my_hensu==12345:
#     print('OK')

#1-2
# last_name='大原'
# first_name='太郎'
# print('{}{}'.format(last_name,first_name))

#2-1
# name_list=['太郎','次郎','三郎','四郎','五郎']
# for i in range(0,5):
#     print(name_list[i])

#2-2
# name=input('名前を入力してください')
# print(name)

#2-3//
# suuti_list=[100,200,300]
# suuti_list[0]+=300
# print(suuti_list[0])

#2-4
# def kansu():
#     print('あなたの名前は太郎です')

# kansu()

#2-5
# def kansu(name):
#     print(name)

# name=input('名前を入力してください:')
# kansu(name)

#2-6
# def kansu(na):
#     print(na)

# name=input('名前を入力してください:')
# kansu(name)

#2-7
# def kansu():
#     name=input('名前を入力してください:')
#     return name

# name=kansu()
# print(name)

#3-1
# def kansu(sutti):
#     def kansu2(sutti):
#         sutti*sutti
#     def kansu3(sutti):
#         sutti-100
#     return sutti+1
    

# sutti=110
# print(kansu(sutti))

#3-2//
# def kansu(suuti):
#     one=1
#     hundred=100
#     def kansu2(suuti):
#         suuti*suuti
#     def kansu3(suuti):
#         suuti-hundred
#     suuti+one

# suuti=110
# print(kansu(suuti))

#4-1
f=open('level4.txt','w')
f.write('私の名前は大原太郎です')
f.close
input('')