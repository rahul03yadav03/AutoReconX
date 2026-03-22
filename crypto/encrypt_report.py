import hashlib

def hash_analyzer():

    try:
        data = input("[+] enter text or password to analyze: ").encode()
        md5_hash = hashlib.md5(data).hexdigest()
        sha1_hash = hashlib.sha1(data).hexdigest()
        sha256_hash = hashlib.sha256(data).hexdigest()


        print("\n[+] Hash Result")
        print(f"MD5:  {md5_hash}")
        print(f"SHA1:  {sha1_hash}")
        print(f"SHA256:  {sha256_hash}")

    except Exception as e:
        print("[-] Error during hash analysis: ",e)
