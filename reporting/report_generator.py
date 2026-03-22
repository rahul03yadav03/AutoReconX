import json
from datetime import datetime
from cryptography.fernet import Fernet


def save_results_encrypted(results, filename="scan_result.json", key=None):
   
    try:
        if key is None:
            key = Fernet.generate_key()
            print("[+] Generated Encryption key: ", key.decode())

        fernet = Fernet(key)

        json_data = json.dumps(results, indent=4).encode()
        encrypted = fernet.encrypt(json_data)

        with open(filename, "wb") as f:
            f.write(encrypted)

        print(f"[+] Encrypted results saved to {filename}")
        return key

    except Exception as e:
        print("[-] Error saving encrypted results: ", e)
        return None


def generate_final_report(result, filename="final_report.txt"):
    
    try:
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report_lines = []   
        report_lines.append("====Scan Report=====")
        report_lines.append(f"Date & time: {now}")
        report_lines.append(f"Target: {result.get('target', 'N/A')}")
        report_lines.append("============\n")

        
        open_ports = result.get("open_ports", [])
        report_lines.append("Open Ports: ")
        if open_ports:
            for port in open_ports:
                report_lines.append(f" - {port}")
        else:
            report_lines.append(" None found")
        report_lines.append("")

        
        ssh_info = result.get("ssh", {})
        report_lines.append("SSH Info: ")
        if ssh_info:
            report_lines.append(f" Username: {ssh_info.get('username', 'N/A')}")
            report_lines.append(f" Login Successful: {ssh_info.get('success', False)}")
        else:
            report_lines.append(" No ssh info collected")
        report_lines.append("")

        
        web_links = result.get("web_links", [])
        report_lines.append("Web Links Found: ")
        if web_links:
            for link in web_links:
                report_lines.append(f" - {link}")
        else:
            report_lines.append("None found")
        report_lines.append("")

        
        smb_shares = result.get("smb_shares", [])
        report_lines.append("SMB Shares: ")
        if smb_shares:
            for share in smb_shares:
                report_lines.append(f" - {share}")
        else:
            report_lines.append(" None found ")
        report_lines.append("=================================\n")

        
        hosts = result.get("hosts", [])
        if hosts:
            report_lines.append("Discovered Hosts: ")
            for host in hosts:
                report_lines.append(f" - {host}")
            report_lines.append("=================================\n")

        
        os_info = result.get("os", {})
        if os_info:
            report_lines.append("OS Detection: ")
            report_lines.append(f" - {os_info}")
            report_lines.append("=================================\n")

        report_text = "\n".join(report_lines)
        print(report_text)

        with open(filename, "w", encoding="utf-8") as f:
            f.write(report_text)

        print(f"[+] Report saved to {filename}")

    except Exception as e:
        print("[-] Error generating report: ", e)
