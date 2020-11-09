import os
import getpass
print("""

""")
while True:
    os.system("tput setaf 12")
    print("""
     ==============================================================================
     |                                                                            |
     |                  WELCOME TO PYTHON AUTOMATION MENU                         |
     |                                                                            |
     ==============================================================================
    
    """)
    os.system("tput setaf 10")
    print("""
    ===========================================================================
    1)Hadoop
    2)AWS
    3)Docker
    4)Websever
    5)Partition
    6)Linux Command
    7)Exit
    ---------------------------------------------------------------------------
    """)
    
    ch=input("Enter your choice :")
    
    if int(ch)==1:
          print("""
      ==========================================================================
      |                                                                        |
      |                       WELCOME TO Hadoop Technology                     |
      |                                                                        |
      ==========================================================================
          """)
          while True:
               print("""
     
          ==========================================================================
     
               Press 1 : Install Hadoop 
               Press 2 : Check Hadoop installation status and @Version
               *Press 3: What you want your Hadoop to be (Master/Slave)?
               Press 4 : Test your Network Connectivity !!
               Press 5 : For Storage and your powers in system to know!!
               *Press 6: Status & Start Hadoop
               Press 7 : Status of Hadoop - Cluster
               Press 8 : Operation in Hadoop Cluster to Do..!!
               *Press 9: For On-Fly increase in Storage to cluster
               Press 10: Information About Hadoop (why and what)
               Press 11: To..Exit...!!

               (         >>Please * are having the pre-requsite to Use<<)
               ==========================================================================
               """)

               ch=input("Enter Your Choice : ")

               if int(ch)==1:
                    print("Hadoop having dependency as JAVA......we are installing it too")
                    os.system("curl http://35.244.242.82/yum/java/el7/x86_64/jdk-8u171-linux-x64.rpm --output jdk-8u171-linux-x64.rpm")
                    os.system("sudo rpm -i jdk-8u171-linux-x64.rpm --force")
                    os.system("curl https://archive.apache.org/dist/hadoop/core/hadoop-1.2.1/hadoop-1.2.1-1.x86_64.rpm --output hadoop-1.2.1-1.x86_64.rpm")
                    os.system("sudo rpm -i hadoop-1.2.1-1.x86_64.rpm --force")
                    os.system("tar -xvf hadoop-1.2.1.tar.gz")
	

               elif int(ch)==3:
 	               print("""
 	               Press 1:)Master node
 	               Press 2:)Slave node
                   Press 3:) Back to Main menu

 	
 	               """)
	       while True:
 	               option=input("Enter Choice :")
 	               if int(option) == 1 :
                         os.system("tput setaf 8")
                         ip=input("Enter your Master IP with port -")
                         fn=input("Name of the Folder(to recieve shared storages): ")
                         os.system("cd ~")
                         os.system("mkdir {0}".format(fn))
                         os.system("cd /etc/hadoop")

                         #os.system("echo '<configuration><property><name>dfs.name.dir</name><value>/`fn`</value></property></configuration>'> hdfs-site.xml")
                         #os.system("echo '<configuration><property><name>fs.default.name</name><value>hdfs://`ip`</value></property></configuration>' core-site.xml")
                         print("Please...wait ....Hadoop Master is Getting READY>>>")
                         os.system("hadoop namenode format")
                         os.system("hadoop-daemon.sh start namenode")
                         os.system("jps")

 	               elif int(option) == 2 :
                         os.system("tput setaf 8")
                         ip=input("Enter your Master IP with port -")
                         fn=input("Name of the Folder(to recieve shared storages): ")
                         os.system("cd ~")
                         os.system("mkdir {0}".format(fn))
                         os.system("cd /etc/hadoop")
                         #os.system("echo '<configuration><property><name>dfs.name.dir</name><value>/`fn`</value></property></configuration>' > hdfs-site.xml")
                         #os.system("echo '<configuration><property><name>fs.default.name</name><value>hdfs://`ip`</value></property></configuration>' core-site.xml")
                         print("Please...wait ....Hadoop SlaveNode is Getting READY>>>")
                         os.system("hadoop-daemon.sh start datanode")
                         os.system("jps")
                    elif int(option) == 3:
                        break
                    else:
 		               print("Enter Valid Number")
 	

               elif int(ch)==2:
                    os.system("tput setaf 8")
                    print("If installed you can check out the Version..!!?")
                    os.system("hadoop version")
 

               elif int(ch)==4:
                    os.system("tput setaf 6")
                    os.system("ping -c 5 8.8.8.8")

               elif int(ch)==5:
                    print("""

 	               Press 1:) Disk Space
 	               Press 2:) Usage of RAM
	               Press 3:) No. of CPU's under usage
 	
 	               """)
	   while True:
                    op=input("Enter Choice :")
                    if int(op) == 1:
                         os.system("clear")
                         os.system("df -hT")
                    elif int(ch)==2:
                         os.system("clear")
                         os.system("free -m")
                    elif int(ch)==3:
                         os.system("clear")
                         os.system("lscpu")
                    else:
                         break 


               elif int(ch)==6:
                    os.system("tput setaf 8")
                    os.system("hadoop namenode format")
                    os.system("hadoop-daemon.sh start namenode")
                    os.system("tput setaf 7")
                    print("hadoop STATUS:")
                    os.system("jps")
 	

               elif int(ch)==7:
                    print("""
 	               Press 1: Detailed view of Cluster
 	               Press 2: Simple view of Cluster
	               Press 3: To Main-menu

 	
 	               """)
	   while True:
                    if int(op) == 1 :
                         os.system("clear")
                         os.system("tput setaf 8")
                         os.system("hadoop dfsadmin -report")
                    elif int(ch)==2:
                         os.system("tput setaf 5")
                         os.system("clear")
                         os.system("hadoop dfsadmin -report | less")
                    elif int(ch)==3:
                         break
                    else:
                         print("Please select with-in Option")
	

               elif int(ch)==8:
                    print("""
           	       Press 1:) Upload file-to-Cluster
           	       Press 2:) Create file to Cluster
          	       Press 3:) Remove file to Cluster
          	       Press 4:) if you Want to Change BlockSzie from default to Upload file
          	       Press 5:) Increase the Disk-size(shared-folder size)
          	       Press 6:) Help on Hadoop Operations
          	       Press 7:) To Main-menu
          
          
           	          """)
	   while True:
                    if int(op) == 1 :
                         os.system("clear")
                         os.system("tput setaf 3")
                         fn=input("Enter your file-name(include-path): ")
                         os.system("hadoop dfsadmin -report | less")
                         os.system("hadoop fs -put {0} /".format(fn))
                         print("HERE is the File Uploaded -- Status -->>")
                         os.system("hadoop fs ls /")

                    elif int(ch)==2:
                         os.system("tput setaf 5")
                         os.system("clear")
                         os.system("hadoop fs -touchz /")
                         print("File is Created...!!")
                         os.system("hadoop fs -ls /")
                    elif int(ch)==3:
                         os.system("tput setaf 7")
                         os.system("clear")
                         re=input("Enter the Filename to remove: ")
                         os.system("hadoop fs rm {0} /".format(re))
                         print("Successfully Removed the File")
                         os.system("hadoop fs -ls /")
                    elif int(ch)==4:
                         os.system("tput setaf 2")
                         os.system("clear")
                         bs=input("Enter the Block-size (in bytes): ")
                         ff=input("Please enter file-name(with Path): ")
                         os.system("hadoop fs -Ddfsblock.size={0} -put {1} /".format(bs,ff))
                         print("Successfully added with Blocksize {0} uploaded the File",format(bs))
                         os.system("hadoop fs -ls /")
                    elif int(ch)==5:
                         pass
                    elif int(ch)==6:
                         os.system("clear")
                         os.system("hadoop fs")
                    elif int(ch)==7:
                         break
                    else:
                         print("Please select with-in Option")
 	


               elif int(ch)==9:
                    pass

               elif int(ch)==10:
                    print('''The Apache™ Hadoop® project develops open-source software for reliable, scalable, distributed computing.

          •The Apache Hadoop software library is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. It is designed to scale up from single servers to thousands of machines, each offering local computation and storage. Rather than rely on hardware to deliver high-availability, the library itself is designed to detect and handle failures at the application layer, so delivering a highly-available service on top of a cluster of computers, each of which may be prone to failures

          >>Hadoop Common: The common utilities that support the other Hadoop modules.
          >> Hadoop Distributed File System (HDFS™): A distributed file system that provides high-throughput access to application data.
          >> Hadoop YARN: A framework for job scheduling and cluster resource management.
          >> Hadoop MapReduce: A YARN-based system for parallel processing of large data sets.
          >> Hadoop Ozone: An object store for Hadoop.

          Who Uses Hadoop?

           A wide variety of companies and organizations use Hadoop for both research and production. Users are encouraged to add themselves to the Hadoop 

          •Scalability

          HADOOP clusters can easily be scaled to any extent by adding additional cluster nodes and thus allows for the growth of Big Data. Also, scaling does not require modifications to application logic.

          • Fault Tolerance

          HADOOP ecosystem has a provision to replicate the input data on to other cluster nodes. That way, in the event of a cluster node failure, data processing can still proceed by using data stored on another cluster node.''')

               elif int(ch)== 11:
                     break
               else :
                    print("Enter Valid Number")

               input("Press Enter To Continue")
               os.system("clear")
 	
    elif int(ch)==2:
                print("""
     ============================================================================
     |                          				                              |
     |                      	WELCOME TO AWS TOOL	                              |
     |                                                   				     |
     ===========================================================================
                """)
                while True:
                    print('''
          ========================================================================
          Press 1:Install AWS CLI software
          Press 2:Check Aws Version
          Press 3:Login To IAM user
          Press 4:EC2 Services
          Press 5:S3 Services
          Press 6:CloudFront Services
          Press 7:Exit
          ------------------------------------------------------------------------
                    ''')
                    ch=input("Enter Your Choice: ")
     
                    if int(ch)==1:
                         while True:
                              print("""
                       Press 1:Windows
                       Press 2:Mac
                       Press 3:Linux
                       Press 4:Exit
                         """)
	       while True:
                              cli=input("Enter Your OS: ")
                              if int(cli)==1:
                                   os.system("pip3 install awscli --upgrade --user")
                                   print("If it is not working properly try to install by GUI.")
                              elif int(cli) == 2:
                                   os.system("curl https://s3.amazonaws.com/aws-cli/awscli-bundle.zip -o awscli-bundle.zip")
                                   os.system("unzip awscli-bundle.zip")
                                   os.system("sudo ./awscli-bundle/install -i /usr/local/aws -b /usr/local/bin/aws")
                              elif int(cli)==3:
                                   os.system("curl https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip -o awscliv2.zip")
                                   os.system("unzip awscliv2.zip")
                                   os.system("sudo ./aws/install")
                                   os.system("sudo ./aws/install -i /usr/local/aws-cli -b /usr/local/bin")
                              elif int(cli)==4:
                                   break
                              else:
                                   print("Invalid Option")

                              input("Enter To continue")
                              os.system("clear")

                    elif int(ch) == 2:
                         os.system("aws --version")

                    elif int(ch)== 3:
                         os.system("aws configure ")


                    elif int(ch)== 4:
                              print("""     

               Press 1:Instances
               Press 2:Volume(EBS)
               Press 3:Network And Security
               Press 4:Key Pair
               Press 5:Exit

                              """)
	while True:
                              op=input("Enter Your Choice:")

                              if int(op)== 1 :
                                   print("""
               ---->Instances
               Press 1:Launch New Instance
               Press 2:View Instances
               Press 3:Start Instance
               Press 4:Stop Instance
               Press 5:Terminate Instance
               Press 6:Reboot Instance
               Press 7:Exit
                              """)
    	while True:
                                   num=input("Enter Your Choice: ")
                                   if int(num)==1:
                                   imgid=input("Enter image ID: ")
                                   instype=input("Enter instance type: ")
                                   keyName=input("Enter your key name: ")
                                   secGrpId=input("Enter security group ID: ")
                                   count=input("Enter number of instances you want: ")
                                   subnetId=input("Enter subnet ID: ")
                                   os.system("aws ec2 run-instances --image-id {0} --instance-type {1} --key-name {2} --security-group-ids {3} --count {4} --subnet-id {5}".format(imgid,instype,keyName,secGrpId,count,subnetId,))

                              elif int(num)==2:
                                   os.system("aws ec2 describe-instances")

                              elif int(num)==3:
                                   inst=input("Enter Instance ID: ")
                                   os.system("aws ec2 start-instances --instance-ids {0}".format(inst))

                              elif int(num)==4:
                                   inst=input("Enter Instance ID: ")
                                   os.system("aws ec2 stop-instances --instance-ids {0}".format(inst))

                              elif int(num)==5:
                                   inst=input("Enter Instance ID: ")
                                   os.system("aws ec2 terminate-instances --instance-ids {0}".format(inst))

                              elif int(num)==6:
                                   inst=input("Enter Instance ID: ")
                                   os.system("aws ec2 reboot-instances --instance-ids {0}".format(inst))
                              elif int(num)==7:
                                   break
                              else:
                                   print("Invalid choice")

                              input("Enter To continue")
                              os.system("clear")  

                    elif int(op)==2 :
                         print("""
               ----->Volumes (EBS)
               Press 1:Create Volume
               Press 2:View Volume
               Press 3:Attach Volume
               Press 4:Dettach Volume
               Press 5:Force Dettach Volume
               Press 6:Delete Volume
               Press 7:Exit
               """)
	while True:
                         vm=input("Enter your Choice: ")

                         if int(vm)==1:
                              zone=input("Enter availability zone (e.g ap-south-1a): ")
                              vtype=input("Enter Volume Type (e.g gp2): ")
                              size=input("Enter EBS volume size : ")
                              os.system("aws ec2 create-volume --availability-zone {0} --volume-type {1} --size {2}".format(zone,vtype,size))

                         elif int(vm)==2:
                              os.system("aws ec2 describe-volumes")

                         elif int(vm)==3:
                              iid=input("Enter Instance ID: ")
                              vid=input("Enter volume ID : ")
                              os.system("aws ec2 attach-volume --instance-id {0} --volume-id {1}".format(iid,vid))

                         elif int(vm)==4:
                              iid=input("Enter Instance ID: ")
                              vid=input("Enter volume ID : ")
                              os.system("aws ec2 detach-volume --instance-id {0} --volume-id {1}".format(iid,vid))                    

                         elif int(vm)==5:
                              iid=input("Enter Instance ID: ")
                              vid=input("Enter volume ID : ")
                              os.system("aws ec2 detach-volume --force --instance-id {0} --volume-id {1}".format(iid,vid))
               
                         elif int(vm)==6:
                              vid=input("Enter volume ID : ")
                              os.system("aws ec2 delete-volume --volume-id {0}".format(vid))

                         elif int(vm)==7:
                              break
                         else:
                              print("Invalid Choice")

                         input("Enter To continue")
                         os.system("clear")
          
          
                    elif int(op)== 3:
                         print("""
               ----->Network And Security
               Press 1:Create Security Group
               Press 2:View All Security Groups Information
               Press 3:View Single Security Groups Information
               Press 4:Delete Security Group
               Press 5:Exit
                         """)
	while True:
                         sg=input("Enter your choice: ")
                         if int(sg)==1:
                              groupname = input("Enter the Security Group name: ")
                              group_description = input("Described by name: ")
                              os.system("aws ec2 create-security-group --group-name {0} --description {1} ".format(groupname,group_description))

                         elif int(sg)==2:
                              os.system("aws ec2 describe-security-groups ")

                         elif int(sg)==3:
                              groupname = input("Enter the Security Group name: ")
                              os.system("aws ec2 describe-security-groups --group-name {}" .format(groupname))

                         elif int(sg)==4:
                              groupname = input("Enter the Security Group name: ")
                              os.system("aws ec2 delete-security-group --group-name {}" .format(groupname))

                         else: break

                         input("Enter To continue")
                         os.system("clear")     

                    elif int(op)== 4:    
                         print("""  
               ----->Key Pairs
               Press 1:Create Key Pairs
               Press 2:View All Key Pairs Information
               Press 3:View Single Key Pair Information 
               Press 4:Delete Key Pair
               Press 5:Exit
               """)
	   while True:
                         key=input("Enter Your Choice: ")

                         if int(key)==1:
                              keyname = input("Enter the key name: ")
                              os.system("aws ec2 create-key-pair  --key-name {0}".format(keyname))

                         elif int(key)==2:
                              os.system("aws ec2 describe-key-pairs")

                         elif int(key)==3:
                              keyname = input("Enter the key name: ")
                              os.system("aws ec2 describe-key-pairs --key-name {0}".format(keyname))

                         elif int(key)==4:
                              keyname = input("Enter the key name: ")
                              os.system("aws ec2 delete-key-pair  --key-name {}".format(keyname))
                         elif int(key)==5:break
                         else:
                              print("Invalid Choice")

        



                    elif int(ch)==5:
                         print("""
          Press 1:Create Bucket
          Press 2:View Bucket List
          Press 3:Delete Bucket
          Press 4:Empty Bucket
          Press 5:Upload Data in Bucket
          Press 6:Exit
                         """)
                         op=input("Enter Your Choice: ")
                         if int(op)==1:
                              bucketName=input("Enter unique bucket name: ")
                              region=input("Enter in which region you want to create bucket (e.g ap-south-1): ")
                              Access=input("Enter access to bucket (e.g public-read): ")
                              os.system("aws s3api create-bucket --bucket {0} --region {1} --acl {2} --create-bucket-configuration LocationConstraint={1}".format(bucketName,region,Access,region))
                         elif int(op)==2 :
                              os.system("aws s3api list-buckets")
                         elif int(op)== 3:
                              print("Note:- Before deleting bucket make sure bucket is empty. You can use option 4 to empty your s3 bucket!")
                              bucketName=input("Enter bucket name: ")
                              region=input("Enter region of bucket (e.g ap-south-1): ")
                              os.system("aws s3api delete-bucket --bucket {0} ".format(bucketName))
                         elif int(op)== 4:
                              print("Note:- This command will remove all objects from bucket!")
                              bucketName=input("Enter bucket name: ")
                              os.system("aws s3 rm s3://{0} --recursive".format(bucketName))
                         elif int(op)== 5:
                              location=input("Enter location of object from your base OS : ")
                              bucketName=input("Enter bucket name: ")
                              Access=input("Enter access to bucket (e.g public-read): ")
                              os.system("aws s3 cp {0} s3://{1} --acl {2}".format(location,bucketName,Access))
                         elif int(op)==6:
                              pass
                         else:
                              print("Invalid Choice")

                         input("Enter To continue")
                         os.system("clear")


                    elif int(ch)== 6:
                         print(""" 
               Press 1:Create Distribution
               Press 2:View Distribution
               Press 3:View Single distribution
               Press 4:Delete Distribution
               Press 5:Exit
                              """)
                         op=input("Enter Your Choice:")
                         if int(op)==1:
                              originName=input("Enter bucket name for distribution (e.g mybucket):")
                              os.system("aws cloudfront create-distribution --origin-domain-name {0}.s3.amazonaws.com".format(originName))
                         elif int(op)==2:
                              os.system("aws cloudfront list-distributions")
                         elif int(op)==3:
                              distId=input("Enter distribution ID: ")
                              os.system("aws cloudfront get-distribution  --id {0} ".format(distId))
                         elif int(op)==4:
                              print("Note:- Before proceding make sure your distribution is disabled!")
                              distId=input("Enter distribution ID: ")
                              ETag=input("Enter eTag of distribution (you can find this in option 3): ")
                              os.system("aws cloudfront delete-distribution  --id {0} --if-match {1}".format(distId,ETag))
                         elif int(op)==5:
                              pass
                         else:
                              print("Invalid Choice")

                         input("Enter To continue")
                         os.system("clear")


                    elif int(ch)== 7:
                         break

                    else:
                         print("Invalid Choice") 

                    input("Enter To continue")
                    os.system("clear")









    elif int(ch)== 3:
          print("""
 ===========================================================================
 |                      		                   		                    |
 |     		         WELCOME TO DOCKER TOOL                       	     |
 |                                                             		     |
 ===========================================================================
        """)

          import os
          os.system("tput setaf 7")
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

                    ch=input("Enter Your Choice : ")


                    if int(ch)==1:
                      os.system("sudo yum install docker  --nobest")


                    elif int(ch)== 2 :
                      print("""
           	    	Press 1: Start Docker Service Permanently 
           	    	Press 2: Stop Docker Service
           	    	Press 3: Show Docker Service Status
          			Press 4: Exit
           		""")
                      while True: 
                          op=input("Enter Choice :")
                          if int(op) == 1 :
                              print("-------------Press Enter To Quit----------")
                              os.system("sudo systemctl start docker")
                              os.system("sudo systemctl enable docker")
                          elif int(op) == 2 :
                              print("-------------Press Enter To Quit----------")
                              os.system("sudo systemctl stop docker")
                          elif int(op) == 3 :
                                  print("-------------Press Enter To Quit----------")
                                  os.system("sudo systemctl status docker")


                          elif int(op) == 4:
                                  break   

                          else:
                              print("Enter Valid Number")
                              input("Enter To continue")
                              os.system("clear")  

                    elif int(ch)==3:
                      os.system("docker -v")


                    elif int(ch)==4:
                      op=input("---->Enter Image Distro Name:")
                      os.system("docker search {0}".format(op))


                    elif int(ch)==5:
                      op=input("---->Enter Image name:")
                      os.system("docker pull {0}".format(op))

                    elif int(ch)==6:
                      os.system("docker images")

                    elif int(ch)==7:
                      op=input("---->Enter Container Name :")
                      img=input("---->Enter OS Image  :")
                      os.system("docker run -it --name {0} {1}".format(op,img))

                    elif int(ch)==8:
                      os.system("docker ps")


                    elif int(ch)==9:
                      os.system("docker ps -a")


                    elif int(ch)==10:
                      op=input("---->Enter Container Name :")
                      os.system("docker start {0}".format(op))
                      os.system("docker attach {0}".format(op))

                    elif int(ch)==11:
                      while True:
                          print("""

           	       Press 1: Delete Single Image
           	       Press 2: Delete All  Images
          	 	  Press 3: Exit
 	 		     """)
                          op=input("------>Enter Your choice(1/2)?:")
                          print(op)

                          if int(op) == 1 :
                              img=input("---->Enter Image Name:")
                              version=input("---->OS version :")
                              os.system("docker rmi -f {0}:{1}".format(img,version))

                          elif int(op) == 2 :
                              print("""
           	                    Started Deleting All Images...
           	              """)
                              os.system("docker rmi `docker images -a -q`")
                              print("""
           	                   All Images Deleted Sucessfully!!! 
           	              """)
                          elif int(op) == 3 :
                              break
                          else:
                              print("Enter Valid Number")
                              input("Enter To continue...")
                              os.system("clear")  
                    elif int(ch)==12:
                      while True: 
                          print("""
           	        	Press 1: Delete Single OS Container
 	                    	Press 2: Delete All OS Container
	 	           	Press 3: Exit
 	 	          		""")
                          op=input("---->Enter Your choice(1/2?):")
                          if int(op) == 1 :
                              containerID=input("---->Enter Container Name(Container ID):")
                              os.system("docker rm -f {0}".format(containerID))
                          elif int(op) == 2 :
                              print("""
 	                           Started Deleting All Containers...
 	                            """)
                              os.system("docker rm `docker ps -a -f -q`")
                              print("""
 	                          All Containers Deleted Sucessfully!!! 
 	                        """)
                          elif int(op) == 3 :
                              break
                          else:
                              print("Enter Valid Number")

                          input("Enter To continue")
                          os.system("clear")  


                    elif int(ch)==13:
                      while True:
                          print("""
           	          Press 1: Exit/Stop Single Container
           	          Press 2: Exit/Stop All Containers
	          	     Press 3: Exit
 	       		""")
                          op=input("---->Enter Your choice(1/2?):")
                          print(op)
                          if int(op)==1 :
                              containerID=input("---->Enter Container Name:")
                              os.system("docker stop {0}".format(containerID))
                          elif int(op)==2 :
                              print("""
 	                          Stopping All Containers...
 	                        """)
                              os.system("docker stop `docker ps -q`")
                              print("""
                                  All Containers stoped Sucessfully!!! 
 	                        """)
                          elif int(op)==3:
                              break
                          else:
                              print("Enter Valid Number")

                              
                          input("Enter To continue")
                          os.system("clear")  

                    elif int(ch)==14:
                         os.system("docker info")

                    elif int(ch)== 15:
                         break
                    else :
                         print("Enter Valid Number")
            
                    input("Enter To continue")
                    os.system("clear")  




    elif int(ch)== 4:
          print("""
 ===========================================================================
 |	                                                                      |
 |       	 	         WELCOME TO  WEBSERVER TOOL                         |
 |                              		       		          	     |
 ===========================================================================
                """)
          os.system("tput setaf 7")
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

               cw=input("Enter your choice : ")
     
               if int (cw) == 1:
          	     os.system("sudo yum install -y httpd")
                    
               elif int (cw) == 2:
                    print("-----------Press Q to quit--------------- ")
                    os.system("sudo systemctl start httpd")
     
               elif int (cw) == 3:
                    print("-----------Press Q to quit--------------- ")
                    os.system("sudo systemctl status httpd")
               elif int (cw) == 4:
                    print("-----------Press Q to quit--------------- ")
                    os.system("sudo systemctl stop httpd")
               elif int (cw) == 5:
                    exit()
               else:
                    print("Option not supported")
               input("Enter to continue....")
               os.system("clear")

    elif int(ch)== 5:
          print("""
 ==========================================================================
 |                     				                                  |
 |          	       	WELCOME TO LVM TOOL                              |
 |                                            				         |
 ==========================================================================
             """)


          while True:
                    os.system("tput setaf 2")
                    ch = int(input('''
             Press 1: To Check Available Disks
             Press 2: To create Physical Volume
             Press 3: Check All Physical Volumes Information
             Press 4: Check Physical Volumes Information By PV Name
             Press 5: To create Volume Groups
             Press 6: Check All Volume Groups Information
             Press 7: Check Volume Groups Information By Name 
             Press 8: To Create Logical Volume
             Press 9: Check All Logical Volume Information
             Press 10 : Check Logical Volume Information By Name
             Press 11: To format Logical Volume
             Press 12: To Mount Logical Volume 
             Press 13: To Extend Logical Volume
             Press 14: To Resize(Format) The Newly Extended Partition
             Press 15: To Extend Volume Group
             Press 16: To Exit

             Enter Your Choice: '''))

                    if ch == 1:
                      os.system("fdisk -l")

                    elif ch==2:
                            print("\n")
                            os.system("tput setaf 7")
                            Disk1 = input("\n\n Enter Name of Disk:")
                            os.system("pvcreate {}" .format(Disk1))
                            os.system("tput setaf 3")
                            print("\n\t\t\t***Physical Volume Created Successfully***")
                            os.system("tput setaf 7")


                    elif ch==3:
                           os.system("pvdisplay")
            

                    elif ch==4:
                           Disk1 = input("\n\n Enter Name of Disk:")
                           os.system("pvdisplay {}" .format(Disk1))



                    elif ch==5:
                             print("\n")
                             os.system("tput setaf 7")
                             Disk1 = input("\n\n Enter the name of 1st PV:")
                             Disk2 = input("\n\n Enter the name of 2st PV:")
                             name1 = input("Enter the name of Volume Group:")
                             os.system("vgcreate {} {} {}" .format(name1,Disk1,Disk2))
                             os.system("vgdisplay {}" .format(name1))
                             os.system("tput setaf 3")
                             print("\n\t\t\t***Volume Group Created Successfully***")
                             os.system("tput setaf 7")


                    elif ch==6:
                           os.system("vgdisplay")   

                    elif ch==7:
                           name1 = input("Enter the name of Volume Group:")
                           os.system("vgdisplay {}".format(name1))


                    elif ch==8:
                             print("\n")
                             os.system("tput setaf 7")
                             name1 = input("Enter the name of Volume Group:")
                             name2 = input("Enter the name of  Logical Volume:")
                             size1 = input("Enter the size in GB for your Logical Volume:")
                             os.system("lvcreate --size {}G --name {} {}" .format(size1,name2,name1))
                             os.system("lvdisplay {}/{}" .format(name1,name2))
                             os.system("tput setaf 3")
                             print("\n\t\t\t***Logical Volume Created Successfully***")
                             os.system("tput setaf 7")
              

                    elif ch==9:
                           os.system("lvdisplay")

                    elif ch==10:
                           name1 = input("Enter the name of Volume Group:")
                           name2 = input("Enter the name of  Logical Volume:")
                           os.system("lvdisplay {}/{}" .format(name1,name2))

                    elif ch==11:
                              print("\n")
                              os.system("tput setaf 7")
                              name1 = input("Enter the name of Volume Group:")
                              name2 = input("Enter the name of  Logical Volume:")
                              os.system("mkfs.ext4 /dev/{}/{}" .format(name1,name2))
                              os.system("tput setaf 3")
                              print("\n\t\t\t***Logical Volume Formatted Successfully***")
                              os.system("tput setaf 7")


                    elif ch==12:
                           while True:
                               nf=int(input("""
                               Press 1:To Mount On New Folder
                               Press 2:To Mount On Existing Folder
                               Press 3:Exit

                               Enter Your Choice :
                               """))
                               if nf==1:
                                   os.system("tput setaf 7")
                                   mount_point = input("Enter New Folder Name:")
                                   os.system("mkdir {}" .format(mount_point))
                                   name1 = input("Enter the name of Volume Group:")
                                   name2 = input("Enter the name of  Logical Volume:")
                                   os.system("mount /dev/{}/{} {}" .format(name1,name2,mount_point))
                                   os.system("df -h")
                                   os.system("tput setaf 3")
                                   print("\n\t\t\t***Logical Volume Mounted Successfully***")

                               elif nf==2:
                                   os.system("tput setaf 7")
                                   mount_point = input("Enter Folder Name:")
                                   name1 = input("Enter the name of Volume Group:")
                                   name2 = input("Enter the name of  Logical Volume:")
                                   os.system("mount /dev/{}/{} {}" .format(name1,name2,mount_point))
                                   os.system("df -h")
                                   os.system("tput setaf 3")
                                   print("\n\t\t\t***Logical Volume Mounted Successfully***")

                               elif nf==3:
                                   break

                               else:
                                   print("Invalid Option")

                                   input("Press Enter To Continue")
                                   os.system("clear")

                    elif ch==13: 
                           print("\n")
                           os.system("tput setaf 7")
                           size1 = input("Enter the size in GB to extend in Logical Volume:")
                           name1 = input("Enter the name of Volume Group:")
                           name2 = input("Enter the name of  Logical Volume:")
                           os.system("lvextend --size +{}G /dev/{}/{}" .format(size1,name1,name2))
                           os.system("tput setaf 3")
                           print("\n\t\t\t***Logical Volume Extended Successfully***")
                           print("\n\t\t\t*** Resize The Volume To Use Extended Storage***")
                           os.system("tput setaf 7")
                           
               
                    elif ch==14:
                          print("\n")
                          os.system("tput setaf 7")
                          name1 = input("Enter the name of Volume Group:")
                          name2 = input("Enter the name of  Logical Volume:")
                          os.system("resize2fs /dev/{}/{}" .format(name1,name2))
                          os.system("tput setaf 3")
                          print("\n\t\t\t***Newly Extended Partition Successfully Formatted***")
                          os.system("tput setaf 7")
                

                    elif ch==15:
                         VgName=input("Enter Volume Group Name:")
                         DiskName=("Enter Disk Name :")
                         os.system("vgextend {} {}".format(VgName,DiskName))

                    elif ch==16:
                         os._exit(1)
            
                    else:    
                         os.system("tput setaf 7")
                         print("\nEnter Valid Number")

                    input("Press Enter To Continue")
                    os.system("clear")


    elif int(ch)== 6:
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
		1)Show Date
		2)Show Time
		3)View IP address
		4)Create Folder
		5)Create File
		6)Edit File
		7)View running services
		8)Open firefox
		9)Show Running Programs
		10)Show Free RAM
		11)Install software
		12)Present Working Directory
		13)Remove Software
		14)exit from menu
	    
          =========================================================
                """)
               ch=input('enter your choice:')
               if int(ch)==1:
                  os.system('cal')
               elif int(ch)==2:
                  os.system('date')

               elif int(ch)==3:
                    os.system('ifconfig')
	
               elif int(ch)==4:
                    p=input("entre folder name:")
                    os.system("mkdir /"+p)
	
               elif int(ch)==5:
                    op=input("Enter File Name:")
                    os.system("touch "+op)
	
               elif int(ch)==6:
                    op=input("Enter File Name:")
                    os.system("gedit "+op)	
		     
               elif int(ch)==7:
                    os.system('netstat -tnlp')
		
               elif int(ch)==8:
                    os.system('firefox')
		
               elif int(ch)==9:
                    os.system('jobs')
		
               elif int(ch)==10:
                    os.system('free -m')
		
               elif int(ch)==11:
                    a=input('enter softwere name ' )
                    os.system('yum install '+a)
		
               elif int(ch)==12:
                    os.system('pwd')
		
               elif int(ch)==13:
                    b=input('enter softwere name ' )
                    os.system('yum remove '+b)

               elif int(ch)==14:
                    break
		
               else:
                    print("Invalid Choice")

               input("Enter To continue")
               os.system("clear")
    elif int(ch)== 7:
         print ("EXIT")
         exit()

    else:
         print("Invalid Choice")              

    input("Press Enter To Continue")
    os.system("clear")
