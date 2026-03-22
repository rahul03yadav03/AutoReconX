import subprocess

def run_nmap(target):
    print("\n[+] Running nmap scan......\n")

    command =[
        "nmap",
        "-sV",
        "-O",
        target


    ]

    try:
        result = subprocess.run(

            command,
            capture_output=True,
            text=True

        )

        print(result.stdout)

    except Exception as error:
        print("Error Running Nmap: ", error)
