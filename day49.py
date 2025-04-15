# file handeling in c
# f = open('myfile2.txt','rb')
#  print(f)
# text =f.read()
# print(text)
# f.close()
# w for write
# r mode is default
# rb for binary file

#  WRITING A File
f =open('myfile.txt', 'a')
f.write('hello world!')
f.close()

with open('myfile.txt', 'a'): 
f:
 f.write("hey i am inside with")
