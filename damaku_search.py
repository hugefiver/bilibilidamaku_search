import sys

def my_output(a):
    n = len(a)
    for i in range(0,n):
        a[i] = "#{0:<5d}  ".format(i+1) + a[i]


#str = input()
infile = input("输入读取的文件名:")
file_object = open(sys.path[0] + '/' + infile,'r',encoding='utf-8')
str = file_object.read()
file_object.close()
#chr = input("输入要检索的关键字:")

ps = str.find('<i>') + 3
pe = str.find('</i>')
str = str[ps:pe]
list1 = str.split('</d>')
for x in range(0,len(list1)):
    ps = list1[x].find('">') + 2
    list1[x] = list1[x][ps:]

while True:
    list2=[]
    chr = input("输入要检索的关键字:")
    if chr == '#exit':
        exit()
    for x in list1:
        if chr in x:
            list2.append(x)
    my_output(list2)
    str2 = '\n'.join(list2)
    print(str2,'\n')

