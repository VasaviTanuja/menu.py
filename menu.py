import os

print("HI")
print("What do you want to use....")

while True:

	print(""" 
		  Press 1 : For using AWS
		  Press 2 : For Docker
		  Press 3 : For Hadoop
		  Press 4 : For LVM
		  Press 5 : For Apache server 
		  Press 6 : To run basic linux commands
		  Press 0 : To quit
	""")


	x=input("Enter your choice: ")
	ch=int(x)

	if (ch==1):
		print("Which services you want to use...")
		while True:
			print(""" 
				Press 1 : To know the version
				Press 2 : To configure AWS
				Press 3 : To use EC2
				Press 4 : To use EBS 
				Press 5 : To use S3
				Press 6 : To use Cloudfront
				Press 7 : To know about any service 
				Press 0 : To come back to previous menu
			""")

			x=input("Enter your choice : ")
			k=int(x)
			
			if (k==1):
				os.system("aws --version") 

			elif (k==2):
				os.system("aws configure")

			elif (k==3):
				print("""
					Press 1 : To create key pair
					Press 2 : To create security group
					Press 3 : To authorize a security group
					Press 4 : To launch a instance
					Press 5 : To start a instance
					Press 6 : To stop a instance
					Press 7 : To terminate a instance
					Press 8 : To see all instances
					Press 0 : To come back to previous menu
				""")
				
				x=input("Enter your choice: ")
				k=int(x)
				
				if (k==1):
					keyname=input("Enter Key name : ") 
					filename=input("Enter the name of file for saving the key : ")
					work="aws ec2 create-key-pair  --key-name {} --query 'KeyMaterial' --output text > {} ".format(keyname,filename)
					os.system(work)

				elif (k==2):
					sgname=input("Enter the name of Security group : ")                                                 
					desc=input("Enter description for the security group : ") 
					work="aws ec2 create-security-group  --group-name {}  --description {}".format(sgname,desc)
					os.system(work)

				elif (k==3):
					sgname=input("Enter the name of Security group : ")                                                 
					work="aws ec2 authorize-security-group-ingress --group-name {} --protocol tcp --port 22 --cidr 0.0.0.0/0".format(sgname)
					os.system(work)

				elif (k==4):
					imgid=input("Enter the Image Id of Instance which you to launch : ")                                
					instype=input("Enter the type of instance you want : ")
					subtype=input("Enter the subnet-id where you want to launch the instance : ")
					sgid=input("Enter the Security group Id for the instance : ")
					count=input("Enter number of instances you want to launch : ")
					key=input("Enter the key name for the instance : ")
					work="aws ec2 run-instances --image-id  {}  --instance-type {} --subnet-id {} --security-group-ids {} --count {} --key-name {}".format(imgid,instype,subtype,sgid,count,key)
					os.system(work)

				elif (k==5):
					insid=input("Enter the Id of the Instance you want to start : ")                                   
					work="aws ec2 start-instances --instance-ids {}".format(insid)
					os.system(work)

				elif (k==6):
					insid=input("Enter the Id of the Instance you want to stop : ")                                     
					work="aws ec2 stop-instances --instance-ids {}".format(insid)
					os.system(work)

				elif (k==7):
					insid=input("Enter the Id of the Instance you want to terminate : ")                                
					print("Do want to terminate the instance",insid)
					con=input("y/n : ")
					if (con==y):
						work="aws ec2 terminate-instances --instance-ids {}".format(insid)
						os.system(work)
					else:
						os.system("aws ec2 terminate-instances help")

				elif (k==8):
					os.system("aws ec2 describe-instances")

				elif (k==0):
					break

				else:
					print("Enter valid input....")
			
			elif (k==4):
				print("""
					Press 1 : To create a new volume 
					Press 2 : To attach a volume to instance
					Press 3 : To detach a volume
					Press 4 : To delete a EBS volume
					Press 0 : To come back to previous menu
				""")
				
				x=input("Enter your choice : ")
				k=int(x)
			
				if (k==1):
					volsize=input("Enter the size of volume you want to create : ")                                     
					avlzone=input("Enter the name of avaliability zone where you want to create the volume : ")
					work="aws ec2 create-volume --size {} --availability-zone  {}".format(volsize,avlzone)
					os.system(work)

				elif (k==2):
					volid=input("Enter the ID of volume you want to use : ")                                          
					insid=input("Enter the Instance Id to which you want to attach this volume : ")
					work="aws ec2 attach-volume  --volume-id {}  --instance-id {}  --device  /dev/sdf".format(volid,insid)
					os.system(work)
			
				elif (k==3):
					volid=input("Enter the ID of volume you want to detach : ")                                        
					work="aws ec2 detach-volume --volume-id {}".format(volid)
					os.sytem(work)

				elif (k==4):
					volid=input("Enter the ID of volume you want to delete : ")                                        
					work="aws ec2 delete-volume --volume-id {}".format(volid)
					os.system(work)

				elif (k==0):
					break
				else:
					print("Enter valid input.....")

			
			elif (k==5):
				print("""
					Press 1 : To create a new S3 bucket
					Press 2 : To list all s3 buckets
					Press 3 : To list things in a S3 bucket
					Press 4 : To remove / delete a bucket
					Press 5 : To remove objects in a bucket
					Press 0 : To come back to previous menu
				""")
				
				x=input("Enter your choice : ")
				k=int(x)
				
				if (k==1):
					s3name=input("Enter a proper name for your bucket : ")                                           
					reg=input("Enter the region where you want to create the bucket : ")
					work="aws s3api create-bucket --bucket-name {} --region {}".format(s3name,reg)
					os.system(work)

				elif (k==2):
					os.system("aws s3 ls")  
				
				elif (k==3):
					buckname=input("Enter the name of s3 Bucket you want to list the things in it : ")              
					work="aws s3 ls s3://{}".format(buckname)
					os.system(work)

				elif (k==4):
					buckname=input("Enter the name of bucket you want to remove : ")   
					work="aws s3 rb s3://{}".format(buckname)
					os.system(work)

				elif (k==5):
					buckname=input("Enter the name of bucket you want to remove : ")   
					objname=input("Enter the name of object you want to remove : ")
					work="aws s3 rb s3://{}/{}".format(buckname,objname)
					os.system(work)
				elif (k==0):
					break
				else:
					print("Enter valid input....")


			elif (x==6):
				print("""
					Press 1 : To create a distribution in cloudfront
					Press 2 : To get the ETag of distribution
					Press 3 : To delete the cloud front distribution
					Press 0 : To come back to previous menu
				""")
				
				x=input("Enter your choice : ")
				k=int(x)

				if (k==1):
					buckname=input("Enter the name of S3 bucket you want to add to the distribution : ")  
					work="aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com".format(buckname)
					os.system(work)

				elif (k==2):
					cdid=input("Enter the ID of distribution whose ETag you want : ")                               
					os.system("aws cloudfront get-distribution-config --id {} --query ETAg".format(cdid))

				elif (k==3):
					cdid=input("Enter the ID of distribution you want to delete : ")               
					etag=input("Enter the Etag of distribution : ")
					work="aws cloudfront delete-distribution --id {} --if-match {}".format(cdid,etag)
					os.system(work)
				elif(k==0):
					break
				else:
					print("Enter valid input....")
			
			
			elif (k==7):
				servicename=input("Enter the name of service you want to know about : ")     
				service="aws {} help".format(servicename)       
				os.system(service)

			elif (k==0):
				break

			else:
				print("Enter Valid Input...")



	elif (ch==2):
		while True:
			print(""" 
				 Press 1 : To install Docker
				 Press 2 : To get image of a OS
				 Press 3 : To see all OS 
				 Press 4 : To run any OS 
				 Press 5 : To start any OS
				 Press 6 : To stop any OS
				 Press 7 : To delete any image
				 Press 0 : To come back to main menu
			""")

			x=input("Enter your choice : ")
			k=int(x)

			if (k==1):
				os.system("yum install docker -ce --nobest")

			elif (k==2):
				imagename=input("Enter the Image name and version : ")
				work="docker pull {}".format(imagename)
				os.system(work)

			elif (k==3):
				os.system("docker ps -a")

			elif (k==4):
				OSname=input("Enter a name for your OS : ")
				imagename=input("Enter the name of image : ")
				work="docker run -it --name {}{}".format(OSname,imagename)
				os.system(work)

			elif (k==5):
				OSname=input("Enter the name of docker OS you want to start : ") 
				work="docker start {}".format(OSname)
				os.system(work)

			elif (k==6):
				OSname=input("Enter the name of docker OS you want to stop : ") 
				work="docker stop {}".format(OSname)
				os.system(work)

			elif (k==7):
				imagename=input("Enter the name of image you want to remove")
				work="docker rmi {}".format(imagename)
				os.system(work)

			elif (k==0):
				break
			else:
				print("Enter Valid Input...")



	elif (ch==3):
		while True:
			print("""
				Press 1 : To open files in hadoop
				Press 2 : To see running services in hadoop
				Press 3 : Set up the name node and start the name node
				Press 4 : Stop the name node
				Press 5 : To see all the nodes in the cluster
				Press 6 : To upload a file into the cluster
				Press 7 : To upload a file in the cluster with different block size
				Press 8 : To edit hdfs-site.xml 
				Press 9 : To edit core-site.xml
				Press 0 : To come back to main menu	
				
			""")
			os.chdir("/etc/hadoop")
			os.system("pwd")
			x=input("Enter your choice : ")
			k=int(x)

			if (k==1):
				os.system("ls")

			elif (k==2):
				os.system("jps")

			elif (k==3):
				os.system("hadoop namenode -format")
				os.system("hadoop-daemon.sh start namenode")

			elif (k==4):
				os.system("hadoop-daemon.sh stop namenode")

			elif (k==5):
				os.system("hadoop dfsadmin -report")

			elif (k==6):
				filename=input("Enter the path of file which you want to upload to the cluster : ")
				os.system("hadoop fs -put {}".format(filename))

			elif (k==7):
				filename=input("Enter the path of file which you want to upload to the cluster : ")
				newsize=input("Enter new block size : ")
				os.system("hadoop -Ddfs.blocksize={}  -put {} ".format(newsize,filename))
			
			elif (k==8):
				os.system("vi hdfs-site.xml")

			elif (k==9):
				os.system("vi core-site.xml")
 
			elif (k==0):
				break

			else:
				print("Enter valid input...") 


			
	elif (ch==4):
		while True:

			print("""
				 press 1 : To see disks and partitions
				 press 2 : To create a physical volume
				 press 3 : To see all physial volumes
			  	 press 4 : To create a volume group
				 press 5 : To see all the volume groups
				 press 6 : To create a logical volume 
				 press 7 : To see all logical volumes
				 press 8 : To format the disk
			 	 press 9 : To increase the size of logical volume
				 press 10 : To decrease the size of logical volume
				 press 11 : To resize the logical volume
				 press 12 : To mount the any partition or volume to local folder
				 press 13 : To unmount any disk 
				 press 14 : To see all disks and the space in it 
			  	 press 15 : To remove the physical volume
				 press 16 : To remove the volume group 
				 press 17 : To remove the logical volume
				 press 0 : To come back to main menu
			""")

			x=input("Enter your choice : ")
			k=int(x)


			if (k==1):
				print("If you want to see all the disks and their partitions enter \"all\" or Enter the name of disk")
				x=input("What do you want to see : ")
				if (x=="all"):
					os.system("fdisk -l")
				else:
					os.system("fdisk -l {}".format(x))


			elif (k==2):	
				dname=input("Enter the name of disk : ")
				work="pvcreate {}".format(dname)
				os.system(work)


			elif (k==3):
				print("press \"all\" if you want to see all physical volumes or Enter the name of physical volume you want to see")
				x=input("What do you want to see : ") 
				if (x=="all"):	
			 		os.system("pvdisplay")
				else:
					os.system("pvdisplay {}".format(x))


			elif (k==4):
				vgname=input("Enter a name for the new volume group :")			
				vgs=input("Enter the name of disks which you want to add the volume group : ")
				work="vgcreate {} {}".format(vgname,vgs)
				os.system(work)


			elif (k==5):
				print("press \"all\" if you want to see all volume groups or Enter the name of volume group you want to see")
				x=input("What do you want to see : ") 

				if (x=="all"):
					os.system("vgdisplay")

				else:
					os.system("vgdisplay {}".format(x))


			elif (k==6):
				lvname=input("Enter the name for your logical volume : ")
				lvsize=input("Enter the size of logical volume you want to create : ")
				vgs=input("Enter name of volume group you want to add to the logical volume : ")
				work="lvcreate --size {} --name {} {}".format(lvsize,lvname,vgs)
				os.system(work)


			elif (k==7):
				print("press \"all\" if you want to see all logical volumes or Enter the name of logical volume you want to see")
				x=input("What do you want to see : ") 
				if (x=="all"):	
			 		os.system("lvdisplay")
				else:
					os.system("lvdisplay {}".format(x))


			elif (k==8):
				dname=input("Enter the path of disk you want to format : ")
				work="mkfs.ext4 {}".format(dname)
				os.system(work)


			elif (k==9):
				lvname=input("Enter the name of logical volume you want to extend : ")
				addsize=input("Enter the size by how much you want to increase the size of lv : ")
				work="lvextend --size +{} {}".format(addsize,lvname)
				os.system(work)


			elif (k==10):
				lvname=input("Enter the name of logical volume you want to reduce : ")
				rmsize=input("Enter the size by how much you want to decrease the size of lv : ")
				work="lvreduce --size -{} {}".format(rmsize,lvname)
				os.system(work)


			elif (k==11):
				lvpath=input("Enter the path of LV you want to resize : ")
				os.system("resize2fs {}".format(lvpath))

			

			elif (k==12):
				fname=input("Enter the folder name you want to mount : ")
				dname=input("Enter the logical volume or physical volume name to which you want to mount the directory : ")
				work="mount {} {}".format(fname,dname)
				os.system(work)


			elif (k==13):
				dpath=input("Enter the path of disk you want to unmount : ")
				work="umount {}".format(dpath)
				os.system(work)


			elif (k==14):
				os.system("df -hT")


			elif (k==15):
				pvname=input("Enter the name of physical volume you want to remove : ")
				os.system("pvremove {}".format(pvname))
				

			elif (k==16):
				vgname=input("Enter the name of volume group you want to remove : ")
				os.system("vgremove {}".format(vgname))
		 
		 
			elif (k==17):
				lvname=input("Enter the name of logical volume you want to remove : ")
				os.system("lvname {}".format(lvname))

			elif (k==0):
				break

			else:
				print("Invalid input....")
	

	elif (ch==5):
		while True:
			print("""
				Press 1 : To configure Yum repo
				Press 2 : Set up Apache web server
				Press 3 : To create a file in html
				Press 4 : To create new file in cgi-bin
				Press 5 : To run html file on web
				Press 6 : To run cgi-bin file on web 
				Press 0 : To come back to main menu
			""")
			x=input("Enter your choice : ")
			k=int(x)
			if (k==1):
				os.system("rpm -ivh epel-release-latest-8.noarch.rpm")

			elif (k==2):
				os.system("yum install httpd")

			elif (k==3):
				os.chdir("/var/www/html/")
				os.system("pwd")
				filename=input("Enter the name of file you want to create : ")
				os.system("gedit {}".format(filename))

			elif (k==4):
				os.chdir("/var/www/cgi-bin/")
				os.system("pwd")
				filename=input("Enter the name of file you want to create : ")
				os.system("gedit {}".format(filename))

			elif (k==5):
				os.chdir("/var/www/html/")
				ip=input("Enter your IP address : ")
				os.system("ls")
				filename=input("Enter the name of file you want to run on web : ")
				os.system("xdg-open http://{}/{}".format(ip,filename))

			elif (k==6):
				os.chdir("/var/www/cgi-bin/")
				ip=input("Enter your IP address : ")
				os.system("ls")		
				filename=input("Enter the name of file you want to run on web : ")
				os.system("xdg-open http://{}/cgi-bin/{}".format(ip,filename))

			elif (k==0):
				break
		
			else:
				print("Enter valid input...")
		

	elif (ch==6):
		while True:
			print("""
				Press 1 : To see date
				Press 2 : To open calendar
				Press 3 : To see your IP address
				Press 4 : To install any software
				Press 5 : To open python intrepreter
				Press 6 : To see storage
				Press 7 : To see the folders attached to volumes
				Press 8 : To stop firewall
				Press 9 : To start firewall 
				Press 0 : To come back to main menu

			""")
			
			x=input("Enter your choice : ")
			k=int(x)
			
			if (k==1):
				os.system("date")

			elif (k==2):
				os.system("cal")

			elif (k==3):
				os.system("ifconfig enp0s3")

			elif (k==4):
				work=input("What do you want to install : ")
				os.system("yum install {}".format(work))

			elif (k==5):
				os.system("python")

			elif (k==6):
				os.system("fdisk -l")

			elif (k==7):
				os.system("df -h")

			elif (k==8):
				os.system("systemctl stop firewalld")
				os.system("systemctl status firewalld")

			elif (k==9):
				os.system("systemctl start firewalld")
				os.system("systemctl status firewalld")

			elif (k==0):
				break
			else:
				print("Enter valid input....")
				
	elif (ch==0):
		break
		
	else:
		print("Enter valid input...")

			 
