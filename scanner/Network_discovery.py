from scapy.all import *


def arp_scan(subnet, timeout=10, verbose=False):
    host = []
    
    try:
        arp_request = ARP(pdst=subnet)
        broadcast = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = broadcast/arp_request
        answered, unanswered = srp(packet, timeout=timeout, verbose=False, iface=None)
        


        for sent, received in answered:
            host.append({"ip": received.psrc, "mac":received.hwsrc})
            if verbose:
                print(f"[+] Host found: {received.psrc} ----> {received.hwsrc}")

    

    except PermissionError:
        print("[!] Root privileges required for ARP scan")
        return[]

    except Exception as e:
        print(f"[!] Error: {e}")


    return host


