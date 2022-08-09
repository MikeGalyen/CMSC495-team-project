from bs4 import BeautifulSoup
import requests
from urllib3.util import url

def main():
    url = "https://www.linkedin.com/jobs/search/?geoId=107024810&keywords=software%20engineer&location=Everett%2C%20Washington%2C%20United%20States"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('a'):
        print(link.get('href'))

def scrape_url(url: str) -> dict:
    """scrape url, return urls with 'http'
    Args:
      url: string of url to scrape"""

    dict_of_results = {
			"scrape_site": url,
            "links": []
            }
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    for link in soup.find_all('a'):
        link_href = link.get('href')
        if str(link_href).startswith('http'):
            dict_of_results['links'].append(link_href)
    return dict_of_results

# This block scrapes links
def links(url: str):
    text_dict = {
            "site": [
                ]
            }
    r = requests.get(url)
    linksoup = BeautifulSoup(r.content, 'html.parser')
    for link_index, link in enumerate(linksoup.find_all('a')):
        # set limit at 100 so it doesn't take forever
        if link_index == 100:
            break
        link_href = link.get('href')
        if str(link_href).startswith('http'):
            try:
                text_dict_info = text(link_href)
                text_dict['site'].append(text_dict_info)
            except:
                print('did not scrape')
    return text_dict['site']

def get_links(url=None):
    if url is None:
        url = 'https://www.freecodecamp.org/news/tag/resume/'
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}
    reqs = requests.get(url, headers=headers)
    soup = BeautifulSoup(reqs.content, 'html.parser')
    links = soup.findAll('h2', {'class': 'post-card-title'})

    links_list = []
    text_list = []

    for p in links:
        try:
            a = p.find('a')['href']
        except:
            continue
        else:
            links_list.append(a)
    return links_list

# This block scrapes the text
def text() -> dict:
    r = requests.get(url)
    textsoup = BeautifulSoup(r.content, 'html.parser')
    title_text = textsoup.find_all("title")
    text_body = textsoup.find_all('p')

    try:
        text_dict_info = {
                "url": url,
                "title": title_text,
                "p": text_body
                }
        new_string = ""
        for i in text_body:
            for j in i:
                for k in j:
                    new_string += str(k)

        text_dict_info["p"] = new_string

    except:
        print('no info found')
    return text_dict_info


if __name__ == "__main__":
    links("https://www.freecodecamp.org/news/tag/resume")
