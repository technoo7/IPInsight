import os
import time

from get_public_ip import get_public_ip
from get_ip_details import get_ip_details

def check_command():
    command = input("Want To Continue? (y,n): ")
    if command == "y":
        print("Restarting the Tool...")
        time.sleep(1)
        Main()
    elif command == "n":
        print("Closing The Tool...")
    else:
        print("The Only Options are y for yes and n for no")
        check_command()

def IPInsight():
    os.system("cls")
    print("""
        ░▀█▀░▒█▀▀█░▀█▀░▒█▄░▒█░▒█▀▀▀█░▀█▀░▒█▀▀█░▒█░▒█░▀▀█▀▀
        ░▒█░░▒█▄▄█░▒█░░▒█▒█▒█░░▀▀▀▄▄░▒█░░▒█░▄▄░▒█▀▀█░░▒█░░
        ░▄█▄░▒█░░░░▄█▄░▒█░░▀█░▒█▄▄▄█░▄█▄░▒█▄▄▀░▒█░▒█░░▒█░░
        
    By Technobeast (@TechnobeastOP on Telegram)             2023
Warning: This Tool Is Strictly Made For Ethical And Educational Purposes Only. Technobeast Should Not Be Responsible For The Tasks Done By This Code.
""")
    print(f"Your Public IP Address Is: {get_public_ip()}\n")
    ip_address = input("Enter an Public IP address ( for example-> 8.8.8.8 ): ")
    get_ip_details(ip_address)
    check_command()

IPInsight()
