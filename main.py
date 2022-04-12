''' Need proxies/vpn rotator '''
import re
import bs4
import requests as requests


url = 'https://pastebin.com/archive'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_3_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'}

response = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')
print(links)

for link in links:
    parsed_link = re.findall('\A<a href="/.{8}">', str(link))
    for link_text in parsed_link:
        if link_text != "[]":
            #title_text = f'<a href="https://pastebin.com/raw/{link_text[10:18]}">{link.text}</a><br>'
            f = open(f"pastes/{link_text[10:18]}", 'w')
            response = requests.get("https://pastebin.com/raw/{link_text[10:18]}")
            soup = bs4.BeautifulSoup(response.text, 'html.parser')
            #print(soup.text)
            f.write(soup.text)

