from sys import platform
import time
from datetime import datetime as dt

#determine which platform the website blocker is running on
#it helps to find the location of the host file in which  undesired websites will be placed

system = platform
website_list = ["www.facebook.com", "www.instagram.com", "www.netflix.com"]
if (system == "Windows"):
    host_path = r"C:\Windows\System32\drivers\etc\hosts"
else: #for Linux and OSX
    host_path = r"/etc/host"

host_temp = "hosts"

redirect = "127.0.0.1"


while True:
    #check if current time is within working hours
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) > dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 17):
        print ("Working hours...")
        #check the host file to see if it contains the list of websites to block
        with open(host_temp, "r+") as file:
            hosts_content = file.read()
            #file.write("\nThe following websites are being added by webbloc Python website blocker\n")
            for website in website_list:
                if website in hosts_content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        print ("Fun hours...")
    time.sleep(5)