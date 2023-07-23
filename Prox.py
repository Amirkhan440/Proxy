import os
import requests
try:
    proxies_url = 'put your proxy list github name for example 👇🏻'
   # https://raw.githubusercontent.com/github_account_name/repo_name/file_name/http.txt'
    proxies_response = requests.get(proxies_url)
    open('http.txt', 'w').write(proxies_response.text)
except Exception as e:
    print("Error fetching the proxy list:", e)
proxies = open('http.txt', 'r').read().splitlines()
def extract_nepal_proxy_info(proxy):
    proxy_info = proxy.split(':')
    ip = proxy_info[0]
    port = proxy_info[1]
    network = proxy_info[2]
    location = proxy_info[3]
    country = proxy_info[4]
    city = proxy_info[5]
    server = proxy_info[6]
    return ip, port, network, location, country, city, server
nepal_proxies = [proxy for proxy in proxies if '.np' in proxy]
if nepal_proxies:
    nepal_proxy_info = extract_nepal_proxy_info(nepal_proxies[0])
    ip, port, network, location, country, city, server = nepal_proxy_info
    print(f"IP: {ip}")
    print(f"Port: {port}")
    print(f"Network: {network}")
    print(f"Location: {location}")
    print(f"Country: {country}")
    print(f"City: {city}")
    print(f"Server: {server}")
else:
    print("No Nepal proxies found in the list.")
