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
 |                                                                       |
 |     		         WELCOME TO DOCKER TOOL                       	     |
 |                                                             		     |
 ===========================================================================
        """)
while True:
                    print("""
 	==========================================================================
 	Press 1: Install/Update Docker 
	Press 2: Docker Service(Required to use docker)
	Press 3: Check Docker Version 
	Press 4: Check Available Versions In Docker Hub by OS Name
	Press 5: Download OS(Docker Images)
	Press 6: Check Downloaded OS(Image) Information
	Press 7: Run New OS
	Press 8: View Running Containers
	Press 9: View Deployed Container History
	Press 10: Start Container(Previously Installed Container)
	Press 11: Delete Downloaded Images
	Press 12: Delete Deployed Containers
	Press 13: Exit Docker Container
	Press 14: Information About Docker
	Press 15: Exit
	==========================================================================
	""")
    
                    pyttsx3.speak("Enter remote system username")
                    uname = input ("Enter remote system username:")
                    pyttsx3.speak("Enter remote system ip")
                    ip = input("Enter remote system IP:")
                    voice()


                    if ((("install" in text) or ("update" in text)) and ("docker" in text )) or ("1" in text) :
                      os.system("ssh {}@{} sudo yum install docker  --nobest".format(uname , ip))


                    elif (("docker" in text) and (("service" in text) or ("services" in text))) or ("2" in text):
                      print("""
           	    	Press 1: Start Docker Service Permanently 
           	    	Press 2: Stop Docker Service
           	    	Press 3: Show Docker Service Status
          			Press 4: Exit
           		""")
                      while True:
                        voice()
                        if (("start" in text) and ("docker" in text) and ("service" in text)) or ("1" in text) :
                              print("-------------Press Enter To Quit----------")
                              os.system("ssh {}@{} sudo systemctl start docker".format(uname , ip))
                              os.system("ssh {}@{} sudo systemctl enable docker".format(uname , ip))
                              
                        elif (("stop" in text) and ("docker" in text) and ("service" in text)) or ("2" in text)  :
                              print("-------------Press Enter To Quit----------")
                              os.system("ssh {}@{} sudo systemctl stop docker".format(uname , ip))
                        elif (("show" in text) or (("docker" in text) and ("service" in text)) or ("status" in text)) or ("3" in text)  :
                                  print("-------------Press Enter To Quit----------")
                                  os.system("ssh {}@{} sudo systemctl status docker".format(uname , ip))
                        elif ("4" in text) or ("exit" in text):
                                  break
                                  
                        else:
                              print("Enter Valid Number")
                        
                        input("Enter To continue")
                        os.system("clear")  

                    elif ("3" in text) or (("docker" in text) and ("version" in text)):
                      os.system("ssh {}@{} docker -v".format(uname , ip))


                    elif ("4" in text) or ((("version" in text) or ("versions" in text)) and ("in" in text) and ("docker" in text) and ("hub" in text)):
                      op=input("---->Enter Image Distro Name:")
                      os.system("ssh {0}@{1}  docker search {2}".format(uname , ip ,op))


                    elif ("5" in text) or (("download" in text) and ("os" in text)) or (("download" in text) and ("docker" in text) and (("image" in text) or ("images" in text))):
                      op=input("---->Enter Image name:")
                      os.system("ssh {0}@{1}  docker pull {2}".format(uname , ip , op))

                    elif ("6" in text) or ((("downloaded" in text) or ("available" in text)) and (("os" in text) or (("image" in text) or ("images" in text)))):
                      os.system("ssh {0}@{1} docker images".format(uname , ip))

                    elif ("7" in text) or (("run" in text) and ("new" in text) and ("os" in text)):
                      op=input("---->Enter Container Name :")
                      img=input("---->Enter OS Image  :")
                      os.system("ssh {0}@{1} docker run -it --name {2} {3}".format(uname , ip , op , img))

                    elif ("8" in text) or ((("view" in text) or ("show" in text)) and ("running" in text) and (("container" in text) or ("containers" in text))):
                      os.system("ssh {0}@{1} docker ps".format(uname , ip))


                    elif ("9" in text) or (("container" in text)and ("history" in text)):
                      os.system("ssh {0}@{1} docker ps -a".format(uname , ip))


                    elif ("10" in text) or (("start" in text) and (("container" in text) or ("containers"in text))):
                      op=input("---->Enter Container Name :")
                      os.system("ssh {0}@{1} docker start {2}".format(uname , ip , op))
                      os.system("ssh {0}@{1} docker attach {2}".format(uname , ip , op))

                    elif ("11" in text) or (("delete" in text) and (("image"in text) or ("images"in text))):
                        while True:
                            print("""
           	       Press 1: Delete Single Image
           	       Press 2: Delete All  Images
          	 	   Press 3: Exit 
                            """)
                            
                            voice()
                            
                            if("1" in text) or ((("delete" in text) or (("remove" in text)) and ("single" in text) and ("image" in text))) :
                              img=input("---->Enter Image Name:")
                              version=input("---->OS version :")
                              os.system("ssh {0}@{1} docker rmi -f {2}:{3}".format(uname , ip ,img,version))
                              
                            elif ("1" in text) or ((("delete" in text) or ("remove" in text)) and ("all" in text) and (("image" in text) or ("images" in text))) :
                              print("""
           	                    Started Deleting All Images...
           	              """)
                              os.system("ssh {0}@{1} docker rmi `docker images -a -q`".format(uname , ip))
                              print("""
           	                   All Images Deleted Sucessfully!!! 
           	              """)
                             
                            elif ("3" in text) or ("exit" in text) :
                              break
                              
                            else:
                              print("Enter Valid Number")
                            input("Enter To continue...")
                            os.system("clear")  
                    
                    elif ("12" in text) or (("delete") in text and (("container" in text) or ("containers" in text))):
                      while True: 
                          print("""
           	        	Press 1: Delete Single OS Container
 	                    Press 2: Delete All OS Container
	 	           	    Press 3: Exit
 	 	          		""")
                          print("Enter Your choice ")
                          voice()                           

                          if ("1" in text) or ((("remove" in text) or ("delete" in text)) and ("single" in text) and (("container" in text) or ("containers" in text))):
                              containerID=input("---->Enter Container Name(Container ID):")
                              os.system("ssh {0}@{1} docker rm -f {2}".format(uname , ip , containerID))
                          elif ("2" in text) or ((("delete" in text) or ("remove" in text)) and ("all" in text) and (("container" in text) or ("containers" in text))):
                              print("""
 	                           Started Deleting All Containers...
 	                            """)
                              os.system("ssh {0}@{1} docker rm `docker ps -a -f -q`".format(uname , ip ))
                              print("""
 	                          All Containers Deleted Sucessfully!!! 
 	                        """)
                          elif ("3" in text) or ("exit" in text) :
                              break
                          else:
                              print("Enter Valid Number")

                          input("Enter To continue")
                          os.system("clear")  


                    elif ("13" in text) or (("exit"  in text) and (("container" in text) or ("containers" in text))):
                      while True:
                          print("""
           	          Press 1: Exit/Stop Single Container
           	          Press 2: Exit/Stop All Containers
	          	      Press 3: Exit
 	       		""")
                          print("---->Enter Your choice(1/2?):")
                          voice()
                          if ("1" in text) or ((("exit" in text) or ("stop" in text)) and ("single" in text) and (("container" in text) or ("containers" in text))) :
                              containerID=input("---->Enter Container Name:")
                              os.system("ssh {0}@{1} docker stop {2}".format(uname , ip , containerID))
                          elif ("2" in text) or ((("exit" in text) or ("stop" in text)) and ("all" in text) and (("container" in text) or ("containers" in text))) :
                              print("""
 	                          Stopping All Containers...
 	                        """)
                              os.system("ssh {0}@{1} docker stop `docker ps -q`".format(uname , ip ))
                              print("""
                                  All Containers stoped Sucessfully!!! 
 	                        """)
                          elif ("3" in text) or ("exit" in text):
                              break
                          else:
                              print("Enter Valid Number")

                              
                          input("Enter To continue")
                          os.system("clear")  

                    elif ("14" in text) or (("information" in text) and ("about" in text) and ("docker" in text)):
                         os.system("ssh {0}@{1} docker info".format(uname , ip ))

                    elif ("15" in text) or ("exit" in text):
                         break
                    else :
                         print("Enter Valid Number")
            
                    input("Enter To continue")
                    os.system("clear")  
