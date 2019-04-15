import bs4
import requests
import base64

class pcStoreCrawler(object):

    def __init__(self, keyword):
        self.keyword = base64.b64encode(keyword).decode()

    def crawl(self):
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.pcstore.com.tw/adm/psearch.htm?store_k_word={}&slt_k_option=1'.format(self.keyword)
        res = requests.get(url, headers=headers)
        res.encoding = 'big5'
        soup = bs4.BeautifulSoup(res.text, "html.parser")
        result = []
        for div in soup.find_all('div', {'id': 'keyad-pro-right3'}):
            result.append(div.find('div', {'class': 'pic2t pic2t_bg'}).text)
        return result

if __name__ == '__main__':
    keyword = input('Please key-in Keyword: ').encode()
    crawler = pcStoreCrawler(keyword)
    result = crawler.crawl()
    for title in result:
        print(title)
