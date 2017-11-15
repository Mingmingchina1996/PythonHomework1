#读取文件中的账号密码
filePassword=[]
fileName=[]
i=0
fileRead=open("information.log","r+")
#for i in range(3):
while 1:
    fileName.append(fileRead.readline().rstrip('\n'))
    filePassword.append(fileRead.readline().rstrip('\n'))
    if fileName[i]=='':               #这里用来判断是否已经读到文件末尾
        break
    i=i+1
fileRead.close()
fileName.pop()
filePassword.pop()
#要求用户输入用户名密码
inputName=input("Please input your name")
flag=0                                     #flag用来标记输入是否正确，输入密码正确flag置为1
if inputName in fileName:
    for j in range(3):
        inputPassword = input("Please input your password")
        inputStation=fileName.index(inputName)
        if filePassword[inputStation]==inputPassword:         #校验输入密码的正确性
            print("Success")
            flag=1
            break
        else:
            print("Wrong Password!")
            continue
    if flag==0:
        print("Erro")
    #else:

else:
    print("Wrong Name")




