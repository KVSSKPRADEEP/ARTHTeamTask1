import getpass
import os
import speech_recognition as sr
import pyttsx3 as pyt
import pyfiglet

def speak(text):
    with sr.Microphone() as source:
        print("listening....")
        audio = r.listen(source)
        print("OK Got it... ")

    ch = r.recognize_google(audio)
    print(ch)


print("""
""")
while True:
    ascii_banner = pyfiglet.figlet_format("AUTOMATION  MENU")
    print(ascii_banner)

    print("""
     ==============================================================================
     |                                                                            |
     |                  WELCOME TO PYTHON AUTOMATION MENU                         |
     |                                                                            |
     ==============================================================================
          """)

    pyt.speak(" WELCOME TO PYTHON AUTOMATION MENU This Is Voice Controlled Automation Menu Program")

    print("""
    ===========================================================================
                                1)Hadoop
                                +2)AWS
                                3)Docker
                                4)Webserver
                                5)Partition
                                6)Linux Command
    ===========================================================================
      """)

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

    if (("partition" in text):
        while True:
            ascii_banner = pyfiglet.figlet_format("PARTITION")
            print(ascii_banner)

            print("""
              ==========================================================================
              |                                                                        |
              |                       WELCOME TO PARTITION                             |
              |                                                                        |
              ==========================================================================
                  """)
            pyt.speak("Welcome to Partition Menu")

            print("""        
                               1) To Check Available Disks
                               2) To create Physical Volume
                               3) To create Volume Groups
                               4) To Create Logical Volume
                               5) To format Logical Volume
                               6) To Mount Logical Volume 
                               7) To Extend Logical Volume
                               8) To Resize Extended Partition
                               9) Exit
                  """)
            break

        voice()
        ch = text
        if ("1" in ch) (("check" in ch) and ("disks" in ch)):
            print("\n")
            pyt.speak("Available Disks are")
            os.system("fdisk -l")

        elif ("2" in ch) or (("create" in ch) and ("physical" in ch)and ("volume" in ch)):
            print("\n")
            pyt.speak("Please Enter Name of Disk")
            Disk1 = input("\nEnter Name of Disk:")
            os.system("pvcreate {}".format(Disk1))
            os.system("pvdisplay")
            pyt.speak("Physical Volume Created Successfully")
            print("\n\t\t\t***Physical Volume Created Successfully***")


        elif ("3" in ch) or (("create" in ch) and ("volume" in ch) and ("group" in ch)):
            print("\n")
            pyt.speak("Please Enter the name of first PV")
            Disk1 = input("\n\n Enter the name of 1st PV:")
            pyt.speak("Please Enter the name of second PV")
            Disk2 = input("\n\n Enter the name of 2st PV:")
            pyt.speak("Please Enter the name of Volume Group")
            name1 = input("Enter the name of Volume Group:")
            os.system("vgcreate {} {} {}".format(name1, Disk1, Disk2))
            os.system("vgdisplay {}".format(name1))
            os.system("vgdisplay")
            pyt.speak("Volume Group Created Successfully")
            print("\n\t\t\t***Volume Group Created Successfully***")


        elif ("4" in ch) or (("create" in ch) and ("logical" in ch) and ("volume" in ch)):
            pyt.speak("Please Enter the name of Volume Group ")
            name1 = input("Enter the name of Volume Group:")
            pyt.speak("Please Enter the name of Logical Volume")
            name2 = input("Enter the name of  Logical Volume:")
            pyt.speak("Please Enter the size in GB for your Logical Volume")
            size1 = input("Enter the size in GB for your Logical Volume:")
            os.system("lvcreate --size {}G --name {} {}".format(size1, name2, name1))
            os.system("lvdisplay {}/{}".format(name1, name2))
            os.system("lvdisplay")
            pyt.speak("Logical Volume Created Successfully")
            print("\n\t\t\t***Logical Volume Created Successfully***")


        elif ("5" in ch) or (("format" in ch) and ("logical" in ch) and ("volume" in ch)):
            print("\n")
            pyt.speak("Please Enter the name of Volume Group")
            name1 = input("Enter the name of Volume Group:")
            pyt.speak("Please Enter the name of  Logical Volume")
            name2 = input("Enter the name of  Logical Volume:")
            os.system("mkfs.ext4 /dev/{}/{}".format(name1, name2))
            pyt.speak("Logical Volume Formatted Successfully")
            print("\n\t\t\t***Logical Volume Formatted Successfully***")


        elif ("6" in ch) or (("mount" in ch) ) and ("logical" in ch) ) and ("volume" in ch))):
            print("\n")
            pyt.speak("Please Enter Folder Name")
            mount_point = input("Enter Folder Name:")
            os.system("mkdir {}".format(mount_point))
            pyt.speak("Please Enter the name of Volume Group")
            name1 = input("Enter the name of Volume Group:")
            pyt.speak("Please Enter the name of  Logical Volume")
            name2 = input("Enter the name of  Logical Volume:")
            os.system("mount /dev/{}/{} {}".format(name1, name2, mount_point))
            os.system("df -h")
            pyt.speak("Logical Volume Mounted Successfully")
            print("\n\t\t\t***Logical Volume Mounted Successfully***")


        elif ("7" in ch) or (("extend" in ch) and ("logical" in ch) and ("volume" in ch)):
            pyt.speak("Please Enter the size in GB to extend in Logical Volume")
            size1 = input("Enter the size in GB to extend in Logical Volume:")
            pyt.speak("Please Enter the name of Volume Group")
            name1 = input("Enter the name of Volume Group:")
            pyt.speak("Please Enter the name of  Logical Volume")
            name2 = input("Enter the name of  Logical Volume:")
            os.system("lvextend --size +{}G /dev/{}/{}".format(size1, name1, name2))
            pyt.speak("Logical Volume Extended Successfully")
            print("\n\t\t\t***Logical Volume Extended Successfully***")
            print("\n\t\t\t*** Resize The Volume To Use Extended Storage***")


        elif ("8" in ch) or (("resize" in ch) and ("extended" in ch) and ("partition" in ch)):
            pyt.speak("Please Enter the name of Volume Group")
            name1 = input("Enter the name of Volume Group:")
            pyt.speak("Please Enter the name of  Logical Volume")
            name2 = input("Enter the name of  Logical Volume:")
            os.system("resize2fs /dev/{}/{}".format(name1, name2))
            pyt.speak("Newly Extended Partition Successfully Formatted")
            print("\n\t\t\t***Newly Extended Partition Successfully Formatted***")


        elif ("9" in ch) or ("exit" in ch)):
            os.system("exit")
            exit()

        else:
            pyt.speak("Please Give Valid Option")
            print("\nInvalid Option")

        print("Enter to continue")
        os.system("cls")





