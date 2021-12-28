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
 ===========================================================================
 |	                                                                      |
 |       	 	         WELCOME TO  WEBSERVER TOOL                         |
 |                              		       		          	     |
 ===========================================================================
                """)
          os.system("color 2")
          while True:
               print("""
	================================================================
     Press 1: To configure webserver
	Press 2: To start webserver
	Press 3: To check status of webserver
	Press 4: To stop webserver
	Press 5: To exit
     ===============================================================
	               """)

               pyttsx3.speak("Enter remote system username")
               uname = input ("Enter remote system username:")
               pyttsx3.speak("Enter remote system ip")
               ip = input("Enter remote system IP:")
               voice()

     
               if ("1" in text) or (("configure" in text) and ("webserver" in text)):
          	     os.system("ssh {0}@{1} sudo yum install -y httpd".format(uname , ip))
                    
               elif ("2" in text) or (("start" in text) and ("webserver" in text)):
                    print("-----------Press Q to quit--------------- ")
                    os.system("ssh {0}@{1} sudo systemctl start httpd".format(uname , ip))
     
               elif ("3" in text) or (("status" in text) and ("webserver" in text)):
                    print("-----------Press Q to quit--------------- ")
                    os.system("ssh {0}@{1} sudo systemctl status httpd".format(uname , ip))
               elif ("4" in text) or (("stop" in text) and ("webserver" in text)):
                    print("-----------Press Q to quit--------------- ")
                    os.system("ssh {0}@{1} sudo systemctl stop httpd".format(uname , ip))
               elif ("5" in text) or ("exit" in text):
                    exit()
               else:
                    print("Option not supported")


               input("Enter to continue....")
               os.system("clear")
