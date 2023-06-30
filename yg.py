import requests
from bs4 import BeautifulSoup

def get_server_info(url):
    try:
        response = requests.head(url, allow_redirects=True)
        server_header = response.headers.get('Server')
        if server_header:
            return f"Server: {server_header}"
        else:
            return "Server information not found."
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {str(e)}"

def scan_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        for link in soup.find_all('a'):
            print(link.get('href'))
    else:
        print('Failed to access the website.')


print("BTW SHIROKO PUNYA GW YA:>")
print("\033[91m[pastikan gunakan https://]")
url = input("MASUKIN KIN BIJI EH MASUKNYAH MASUKIN URL:")
#YANG BENER RECODE NYAH KALO EROR BUKAN SALAH GWH YA
print(" \33[0;32m ")
print("====================================================================")
print("                   WebSite : nggak ada                        ")
print("                   Channel : @Mrcupu                      ")
print("                 Developers : Kita bersama               ")
print("                          Thank's                          ")
print(" ====================================================================")
print(" \33[0;36m ")
#sedikit info situs web
print("jangan di buat ddos ygy")
print("####################################################################")
SERVER = get_server_info(url)
print(SERVER)
print("####################################################################")
#shiroko #my waifu:)

print("UNTUK INFORMASI TAMBAHAN ADA DI BAWAH INI")
print(" \33[0;34m ")
print("====================================================================")
scan_website(url)


print("====================================================================")






print("[JANGAN DI BUAT DDOS ANJIME DOSA LU:(]")


