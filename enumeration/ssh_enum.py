import paramiko
import socket

def ssh_enum(target):

    print("\n[+] Stating SSh Enumeration...")
    print("[+] Target: ", target)

    username = input("[+] Enter SSH Username: ")
    password = input("[+] Enter SSH Password: ")

    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        print("\n[+] Attempting SSH Login.....")

        client.connect(
            hostname=target,
            username=username,
            password= password,
            timeout=5

        )

        print("[+] SSH Login Successful!")
        print("[+] username: ", username)

        client.close()

    except paramiko.AuthenticationException:
        print("[-] Authentication Failed")

    except paramiko.SSHException as sshException:
        print("[-] SSH Error: ", sshException)

    except socket.timeout:
        print("[-] Connection Timeout")

    except Exception as e:
        print("[-] Error: ", e)
