import requests
from datetime import datetime

sites = ["https://www.google.com", "https://www.github.com", "https://www.siteinexistente12345.com"]

with open("status.txt", "w") as f:
    f.write(f"--- Relatório de Conectividade (Python) ---\n")
    f.write(f"Data: {datetime.now()}\n\n")
    
    for site in sites:
        try:
            response = requests.get(site, timeout=5)
            if response.status_code == 200:
                f.write(f"{site}: Online\n")
            else:
                f.write(f"{site}: Status {response.status_code}\n")
        except requests.exceptions.RequestException:
            f.write(f"{site}: Offline\n")
