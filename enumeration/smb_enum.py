import subprocess

def smb_enum(target):
    print("\n[+] Starting SMB Share Enumeration...")
    print("[+] Target: ",target)

    try:
        command =[
            "nmap",
            "-p", "445",
            "--script", "smb-enum-shares",
            target

        ]

        result = subprocess.run(command, capture_output=True, text=True)

        print("\n[+] SMB Enumeration Result: \n ")
        print(result.stdout)

    except Exception as e:
        print("[-] Error running SMB enumeration: ",e)
