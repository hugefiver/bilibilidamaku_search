import sys

#str = input()
infile = input("输入读取的文件名:")
file_object = open(sys.path[0] + '/' + infile,'r',encoding='utf-8')
str = file_object.read()
file_object.close()
chr = input("输入要检索的关键字:")

ps = str.find('<i>') + 3
pe = str.find('</i>')
str = str[ps:pe]
list1 = str.split('</d>')
for x in range(0,len(list1)):
    ps = list1[x].find('">') + 2
    list1[x] = list1[x][ps:]
list2=[]
for x in list1:
    if chr in x:
        list2.append(x)
str2 = '\n'.join(list2)
print(str2)
