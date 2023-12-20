import requests
from bs4 import BeautifulSoup
import re

def get_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; Media Center PC 6.0; InfoPath.2; MS-RTC LM 8'
        }
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return 'error'

def parse_page(html, return_list):
    soup = BeautifulSoup(html, 'html.parser')
    day_list = soup.find('ul', 't clearfix').find_all('li')
    for day in day_list:
        date = day.find('h1').get_text()
        wea = day.find('p', 'wea').get_text()
        if day.find('p', 'tem').find('span'):
            hightem = day.find('p', 'tem').find('span').get_text()
        else:
            hightem = ''
        lowtem = day.find('p', 'tem').find('i').get_text()
        level = day.find('p', 'win').find('i').get_text()
        return_list.append([date, wea, lowtem, hightem, level])

def print_res(city, return_list):
    tplt = '{0:<10}\t{1:^10}\t{2:^10}\t{3:{5}^10}\t{4:{5}^5}'
    print(f"\t\t{city}:")
    print(tplt.format('日期', '天气', '最低温', '最高温', '风力', chr(12288)))
    for i in return_list:
        print(tplt.format(i[0], i[1], i[2], i[3], i[4], chr(12288)))

def main():
    city_mapping ={
    '101200101': '武汉',
    '101200102': '蔡甸',
    '101201601': '仙桃',
    '101201101': '十堰',
    '101201102': '竹溪',
    '101200701': '咸宁',
    '101200702': '赤壁',
    '101201501': '天门',
    '101200401': '孝感',
    '101200402': '安陆',
    '101200901': '宜昌',
    '101200902': '远安',
    '101201001': '恩施',
    '101201002': '利川',
    '101201701': '潜江',
    '101201201': '神农架',
    '101200801': '荆州',
    '101200802': '江陵',
    '101201401': '荆门',
    '101201402': '钟祥',
    '101200201': '襄阳',
    '101200202': '襄州',
    '101200301': '鄂州',
    '101200302': '梁子湖',
    '101201301': '随州',
    '101201302': '广水',
    '101200501': '黄冈',
    '101200502': '红安',
    '101200601': '黄石',
    '101200602': '大冶'
}

    parameters = [    '101200101', '101200102', '101201601', '101201101',
                      '101201102', '101200701', '101200702', '101201501',
                      '101200401', '101200402', '101200901', '101200902',
                      '101201001', '101201002', '101201701', '101201201',
                      '101200801', '101200802', '101201401', '101201402',
                      '101200201', '101200202', '101200301', '101200302',
                      '101201301', '101201302', '101200501', '101200502',
                      '101200601', '101200602']

    for param in parameters:
        url = f'http://www.weather.com.cn/weather/{param}.shtml'
        html = get_page(url)
        wea_list = []
        parse_page(html, wea_list)
        city_name = city_mapping.get(param, 'Unknown')
        print_res(city_name, wea_list)
        print("\n")

if __name__ == "__main__":
    main()
