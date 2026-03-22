import requests
from bs4 import BeautifulSoup


def web_enum(target):

    if not target.startswith("http://") and not target.startswith("https://"):
        url = f"http://{target}"

    else:
        url = target

    print("\n[+] Starting Web Enumeration....")
    print("[+] Target URL: ", url)

    try:
        response = requests.get(url, timeout=5)

        if response.status_code !=200:
            print("[-] Website not reachable or not returning HTTP 200")
            return

        print("[+] Status Code: ", response.status_code)

        soup = BeautifulSoup(response.text, "html.parser")

        if soup.title:
            print("[+] Page Title: ",soup.title.string)

        else:
            print("[+] Page Title: Not Found")

        links = soup.find_all("a")

        if  not links:
            print("[-] NO links found")

        for link in links:
            href = link.get("href")
            if href:
                print("-", href)

    except requests.exceptions.ConnectionError:
        print("[-] Target is not a web server")

    except requests.exceptions.RequestException as e:
        print("[-] REquest error: ",e)









                
