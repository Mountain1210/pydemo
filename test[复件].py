def test(a,b):
	print("%d"%(a+b))



test(11,12)



# f=open('text.txt','w')
# f.write("Hello world, I am Iron man")
# f.close();


# f=open('test.txt','r')

# content=f.read(5);

# print(content)

# print("-"*30)

# content=f.read();

# print(content)

# f.close();


f=open('text.txt','r')

content=f.readline()

print(type(content));


i=1

for temp in content:
	print("%d:%s"%(i,temp))
	i+=1

f.close()