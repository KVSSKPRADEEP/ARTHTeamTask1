import os
import speech_recognition as sr
import pyttsx3
os.system("cls")



def voice():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        pyttsx3.speak("Please enter option name . We are listening your commands")
        print("Please enter option")
        pyttsx3.speak("Give clear voice input for better results")
        print("Give clear voice input for better results")
        mysound = r.listen(source)
        global text
        text = r.recognize_google(mysound)
        text = text.lower()
        print("Got it....\n Your provided command is :" + text)



print("""
 ==========================================================================
 |                    	                                                 |
 |	              WELCOME TO LINUX PROGRAMS TOOLS                        |
 |                        				                             |
 ==========================================================================
            """)
 while True:

               print("""
         ======================================================= 
		1)Show Calendar
		2)Show Date and Time
		3)View IP address
		4)Create Folder
        5)Delete Folder
		6)Create File
        7)Delete File
		8)Edit File
		9)View running services
		10)Open firefox
		11)Show Running Programs
		12)Show Free RAM
		13)Install software
		14)Present Working Directory
		15)Remove Software
		16)exit from menu
	    
          =========================================================
                """)
               voice() 
               #ch=input('enter your choice:')
               if ("1" in text) or ("cal" in text):
                  os.system('cal')
               elif ("2" in text) or ("date" in text) or ("time" in text):
                  os.system('date')

               elif ("3" in text) or ("ip"  in text):
                    os.system('ifconfig')
	
               elif ("4" in text) or (("create" in text) and ("folder" in text)):
                    p=input("entre folder name:")
                    os.system("mkdir /"+p)

               elif ("5" in text) or (("delete" in text) and ("folder" in text)):
                    p=input("entre folder name:")
                    os.system("rmdir -rf /"+p)
	
               elif ("6" in text) or (("create" in text) and ("file" in text)) :
                    op=input("Enter File Name:")
                    os.system("touch "+op)

               elif ("7"  in text) or (("delete" in text)("file") in text):
                    op=input("Enter File Name:")
                    os.system("rm -rf "+op)
	
               elif ("8"  in text) or (("edit" in text) and ("file" in text)):
                    op=input("Enter File Name:")
                    os.system("gedit "+op)	
		     
               elif ("9") or (("running" in text) and ("services" in text)):
                    os.system('netstat -tnlp')	

               elif ("10" in text) or  ("firefox" in text):
                    os.system('firefox')
		
               elif ("11" in text) or (("running" in text) and (("program" in text) or ("programs" in text))):
                    os.system('jobs')
		
               elif ("12" in text) or (("free" in text) and ("ram" in text)):
                    os.system('free -m')
		
               elif ("13" in text) or (("install" in text) and ("software" in text)):
                    a=input('enter software name ' )
                    os.system('yum install '+a)
		
               elif ("14" in text) or (("working" in text) and ("directory" in text)):
                    os.system('pwd')
		
               elif ("15" in text) or (("remove" in text) and ("software" in text)):
                    b=input('enter softwere name ' )
                    os.system('yum remove '+b)

               elif ("16" in text) or ("exit" in text):
                    break
		
               else:
                    print("Invalid Choice")

               input("Enter To continue")
               os.system("clear")
