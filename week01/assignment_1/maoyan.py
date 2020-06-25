import requests
import pandas as pd
from bs4 import BeautifulSoup


headers ={
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Cookie': '__mta=45372059.1592975274690.1593003755360.1593003768474.14; uuid_n_v=v1; uuid=A798BDF0B5D811EA80F64D80EBA969F7D9F0D8E1CD5B4A97AA3E58E0A6FA9B9E; _lx_utm=utm_source%3Dbing%26utm_medium%3Dorganic; _lxsdk_cuid=172e4b9b24ec8-01665d5c4f0f37-79657964-1fa400-172e4b9b24fc8; _lxsdk=A798BDF0B5D811EA80F64D80EBA969F7D9F0D8E1CD5B4A97AA3E58E0A6FA9B9E; mojo-uuid=b357b830fdd51d9c7accd4de3374c492; _csrf=d7745970ca7b89c98a6556a18264247ed8090e10465fbc1928dc85d0cb7f874a; mojo-session-id={"id":"ae0cda5afb653af666dd332ff1b9df63","time":1593003754824}; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1592975275,1593003755; __mta=45372059.1592975274690.1592976431715.1593003755360.13; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593003768; mojo-trace-id=4; _lxsdk_s=172e66c45ef-b3-9ee-308%7C%7C5',
    'Host': 'maoyan.com',
    'Referer': 'https://maoyan.com/board',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36 Edg/83.0.478.54'
}

myurl = 'https://maoyan.com/board/4'
response = requests.get(myurl, headers=headers)


soup = BeautifulSoup(response.text, 'html.parser')

movielist = []

for movie in soup.find_all('div', attrs={'class': 'board-item-content'}):
    name = movie.find('a').text
    released_time = movie.find('p', attrs={'class': 'releasetime'}).text
    score = movie.find('i', attrs={'class': 'integer'}).text + movie.find('i', attrs={'class': 'fraction'}).text

    movielist.append([name, released_time, score])

movies = pd.DataFrame(data=movielist)
movies.to_csv('./maoyantop10.csv', encoding='gbk', header=False, index=False)
    
