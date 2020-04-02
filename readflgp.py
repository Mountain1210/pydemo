#coding=utf-8

f=open('test.txt','r')

str=f.read(3)

print('读取的数据是：',str)

position=f.tell();

print('当前文件位置：',position);

str=f.read(3)

print('读取的数据是：',str)

position=f.tell()

print('当前文件位置：',position)


f.close();