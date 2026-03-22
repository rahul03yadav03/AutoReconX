import socket
import threading

def port_scanner(target, start_port, end_port):
    """
    Scan ports on target from start_port to end_port
    Returns list of open ports
    """
    open_ports = []
    threads = []
    
    def scan_single_port(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)  # Reduced timeout for faster scanning
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is OPEN")
            open_ports.append(port)
        s.close()
    
    # Create threads for all ports
    for port in range(start_port, end_port + 1):
        t = threading.Thread(target=scan_single_port, args=(port,))
        threads.append(t)
        t.start()
    
    # Wait for all threads to complete
    for t in threads:
        t.join()
    
    print("Scanning Finished")
    return open_ports


# Keep this for standalone usage (optional)
if __name__ == "__main__":
    target = input("Please enter your target: ")
    starting_port = int(input("Please enter starting port number: "))
    ending_port = int(input("Please enter ending port number: "))
    
    open_ports = port_scanner(target, starting_port, ending_port)
    print(f"Open ports found: {open_ports}")
