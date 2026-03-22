import argparse
import sys
import os
import re


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


from scanner.port_scanner import port_scanner
from scanner.Network_discovery import arp_scan
from scanner.Os_detector import run_nmap


from enumeration.web_enum import web_enum
from enumeration.smb_enum import smb_enum
from enumeration.ssh_enum import ssh_enum


from reporting.report_generator import save_results_encrypted, generate_final_report


from crypto.encrypt_report import hash_analyzer



def validate_ip(ip):
    pattern = r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
    if not re.match(pattern, ip):
        return False
    for octet in ip.split("."):
        if int(octet) > 255:
            return False
    return True


def get_interactive_input():
    """Get target and ports from user interactively"""
    print("\n=== AutoReconX Interactive Mode ===")
    target = input("Please enter your target: ")
    
    while not validate_ip(target):
        print("[-] Invalid IP format")
        target = input("Please enter your target: ")
    
    port_range = input("Please enter port range (default 1-2000): ").strip()
    if not port_range:
        port_range = "1-2000"
    
    return target, port_range


def parse_ports(port_str):
    """Parse port range string like '1-100'"""
    try:
        if "-" in port_str:
            start, end = map(int, port_str.split("-"))
            return start, end
        else:
            return 1, 2000
    except:
        return 1, 2000


def main():
    parser = argparse.ArgumentParser(
        description="AutoReconX - Automated Recon Tool"
    )

    parser.add_argument("target", nargs="?", help="Target IP Address")
    parser.add_argument(
        "-p",
        "--ports",
        default="1-2000",
        help="Port range (example 1-2000)"
    )
    parser.add_argument("--web", action="store_true", help="Run web enumeration")
    parser.add_argument("--smb", action="store_true", help="Run SMB enumeration")
    parser.add_argument("--ssh", action="store_true", help="Run SSH enumeration")
    parser.add_argument("--os", action="store_true", help="Detect operating system")
    parser.add_argument("--arp", help="Run ARP scan (example 192.168.1.0/24)")
    parser.add_argument(
        "-o",
        "--output",
        default="scan_report.txt",
        help="Save report file"
    )

    args = parser.parse_args()
    results = {}

   
    if args.arp:
        print("[+] Running Network Discovery...")
        hosts = arp_scan(args.arp, verbose=True)
        results["hosts"] = hosts
        generate_final_report(results, args.output) 
        return

    
    if args.target is None:
        target, port_range = get_interactive_input()
        args.target = target
        args.ports = port_range
        args.web = True
        args.smb = True
        args.ssh = True
        args.os = True
    else:
        
        if not validate_ip(args.target):
            print("[-] Invalid IP")
            sys.exit(1)

    target = args.target
    print(f"\n[+] Target: {target}")
    results["target"] = target

    
    start, end = parse_ports(args.ports)

    
    print("[+] Running Port Scan...")
    open_ports = port_scanner(target, start, end)
    results["open_ports"] = open_ports

    
    if args.os:
        print("[+] Detecting OS...")
        os_info = run_nmap(target)
        results["os"] = os_info

    
    if args.web:
        print("[+] Running Web Enumeration...")
        web_links = web_enum(target)
        results["web_links"] = web_links

    
    if args.smb:
        print("[+] Running SMB Enumeration...")
        smb_shares = smb_enum(target)
        results["smb_shares"] = smb_shares

    
    if args.ssh:
        print("[+] Running SSH Enumeration...")
        ssh_info = ssh_enum(target)
        results["ssh"] = ssh_info

    
    print("\n[+] Generating Report...")
    generate_final_report(results, args.output)

    
    try:
        save_results_encrypted(results)
    except Exception as e:
        print(f"[-] Could not encrypt report: {e}")

    print("\n[+] Recon Completed")


if __name__ == "__main__":
    main()
