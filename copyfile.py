#coding=utf-8


oldFileName = input("请输入要拷贝的文件名字:")


oldFile=open(oldFileName,'r')

if oldFile:
	fileFlagNum=oldFileName.rfind('.')

	if fileFlagNum>0:
		fileFlag=oldFileName[fileFlagNum:]

	newFileName=oldFileName[:fileFlagNum]+'[复件]'+fileFlag

	newFile=open(newFileName,'w')

	for lineContent in oldFile.readlines():	
		newFile.write(lineContent)


	oldFile.close()
	newFile.close()