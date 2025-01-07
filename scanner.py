import socket
#IPs
start_ip = "192.168.0.1"
end_ip = "192.168.0.255"
#Into octets
start_octet = start_ip.split(".")
end_octet = end_ip.split(".")
#conversion to integers
start_octet = [int(octet) for octet in start_octet]
start_octets[3] += 1
end_octet = [int(octet) for octet in end_octet]
#initialize
current_octet = start_octets[:]
#socket object
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#timeout
sock.settimeout(0.5)
#Scan IPs
while current_octet != end_octet:

    #Construct the IP
    current_ip = ".".join([str(octet) for octet in current_octet])
    #Try to connect
    result = sock.connect_ex((current_ip, 80))
    #If success
    if result == 0:
        print(f"IP {current_ip} is up")

    #Increment the current IP
    current_octet[3] += 1

    #if the current octet is 255
    for i in range(3, 0, -1):
        if current_octet[i] == 256:
            current_octet[i] = 0
            current_octet[i-1] += 1
        
#close socket
s.close()