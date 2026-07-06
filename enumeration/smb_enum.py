import subprocess
import colorama
colorama.init(autoreset=True)


def smb_enum(target):
    print(colorama.Fore.GREEN  + "\n[+] Starting SMB Share Enumeration...")
    print(colorama.Fore.BLUE + "[+] Target: ",target)

    try:
        command =[
            "nmap",
            "-p", "445",
            "--script", "smb-enum-shares",
            target

        ]

        result = subprocess.run(command, capture_output=True, text=True)

        print(colorama.Fore.GREEN + "\n[+] SMB Enumeration Result: \n ")
        print(colorama.Fore.WHITE + result.stdout)

    except Exception as e:
        print(colorama.Fore.RED + "[-] Error running SMB enumeration: ",e)
