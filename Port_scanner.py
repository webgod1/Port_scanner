import socket
import sys
import pyfiglet
import os
from datetime import datetime
from colorama import Fore,Style,init


init(autoreset=True)
#these banner is for fancy and more advance cli look
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner_port():
        banner = pyfiglet.figlet_format('Port Scanner', font='big')
        print(Style.BRIGHT + Fore.LIGHTGREEN_EX + banner)
        # print(banner)


file = open("port_result.txt", "w")

def main():
    clear_screen()
    banner_port()
    print(Fore.LIGHTBLACK_EX + "=" * 50)
    print(Fore.GREEN + "🔥 Author: " + Fore.LIGHTGREEN_EX + "Yaro Godwin")
    print(Fore.GREEN + "🌍 GitHub: " + Fore.LIGHTGREEN_EX  + "https://github.com/webgod1")
    print(Fore.GREEN + "🛠  Version:" + Fore.GREEN + " Version 1.0")
    print(Fore.GREEN + "📜 Description: " + Fore.LIGHTWHITE_EX + "This script is a simple Python-based port scanner designed to quickly identify open ports on a target machine. Built using socket programming for efficiency and ease of use.")
    print(Fore.LIGHTBLACK_EX + "=" * 50)
    print(Style.RESET_ALL)  # Reset colors
    target = input(Fore.LIGHTGREEN_EX + "\n💻 Enter Target IP Address: " + Fore.WHITE)
    range_of = int(input('Enter Range to scan 1-60000: '))
    host = socket.gethostbyname(target)
    print('')
    print(f"Target: {target}")
    print(f"Host: {host}")
    print('')
    date = datetime.date(datetime.now())

    start_time = datetime.now()
    print(f"Start Time is: {start_time.strftime("%H:%M:%S")}")

    file.write(f"Start Time is: {start_time.strftime("%H:%M:%S")} \n\n")
    #checking for the port
    print("")

    try:
        for port in range(0, range_of):
            SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            SOCKET.settimeout(0.001)
            result = SOCKET.connect_ex((host, port))

            if result == 0:
                try:
                    print(f'Port {port} is open || Service name: {socket.getservbyport(port, 'tcp')}')
                    file.write(f'Port {port} is open || Service name: {socket.getservbyport(port, 'tcp')} \n')
                except socket.error:
                    print(f'Port {port} is open || Service name: {"Unknown"}')
                    file.write(f'Port {port} is open || Service name: {"Unknown"} \n')
            else:
                try:
                    print(f'Port {port} is closed || Service name: {socket.getservbyport(port, 'tcp')}')
                    file.write(f'Port {port} is closed || Service name: {socket.getservbyport(port, 'tcp')} \n')
                except socket.error:
                    print(f'Port {port} is closed || Service name: {"Unknown"}')
                    file.write(f'Port {port} is closed || Service name: {"Unknown"} \n')
    except socket.gaierror:
        print('HOST COULD NOT BE REACHED, EXISTING........!!!')
        file.write("\n\nHOST COULD NOT BE REACHED, EXISTING........!!!")
        sys.exit()

    except socket.error:
        print("Could not connect to server, Existing......!!!")
        file.write("\n\nCould not connect to server, Existing......!!!")
        sys.exit()
    print('')
    end_time = datetime.now()
    print(f"End Time is: {end_time.strftime("%H:%M:%S")}")

    file.write(f"\n End Time is: {end_time.strftime("%H:%M:%S")} \n\n")
    print("")
    total_time = end_time - start_time

    file.write(f"Total Time is: {total_time}")
    print(f"Total time of Scan is: {total_time}")

main()