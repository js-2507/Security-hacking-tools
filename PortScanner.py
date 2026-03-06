#scans ports on a given ip address
import socket
import subprocess
import platform

def ping(target):
    param = '-n' if platform.system().lower() == 'windows' else '-c'
    command = ['ping', param, '1', target]
    return subprocess.call(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL) == 0

def portScanner(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    if s.connect_ex((target, port)):
        print("Port", port, "is closed.")
    else:
        print("Port", port, "is open.")
    s.close()

if __name__=="__main__":
    while True:
        while True:
            target = input("Enter target IP address to scan: ")
            if ping(target):
               print("Host", target, "is successfully reachable.")
               break
            else:
                print("Target is not reachable. Please enter another IP address or check connectivity.")
        while True:
            try:
                choice = int(input("Enter '1' to scan a single port, or '2' to scan a range of ports: "))
                if(choice==1):
                    port = int(input("Enter port to scan: "))
                if choice==2:
                    scanStart = int(input("Enter the starting port: "))
                    scanEnd = int(input("Enter the ending port: "))
                while choice!=1 and choice!=2:
                    choice = int(input("Please enter '1' to scan a single port, or '2' to scan a range of ports: "))
                if choice==1:
                    portScanner(target, port)
                    break
                if choice==2:
                    for i in range(scanStart, scanEnd+1):
                        portScanner(target, i)
                    break
            except ValueError:
                print("Please enter a valid number.")
            except KeyboardInterrupt:
                print("Stopped by user.")
            except Exception as e:
                print("Unexpected error.")
        again = input("Enter 'Y' to try another scan, or any other key to exit: ")
        try:
            if again!="y" and again!="Y":
                print("Goodbye.")
                break
        except ValueError:
            print("Please enter a valid character.")
        except KeyboardInterrupt:
            print("Stopped by user.")
        except Exception as e:
            print("Unexpected error.")