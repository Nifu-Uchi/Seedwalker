import lxml.html
import requests

target_url = 'http://www.sankei.com/politics/news/180316/plt1803160027-n1.html'
target_html = requests.get(target_url).text
root = lxml.html.fromstring(target_html)
#text_content()メソッドはそのタグ以下にあるすべてのテキストを取得する
root.cssselect('#fontMiddiumText > p').text_content()