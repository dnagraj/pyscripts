from flask import Flask, request
import requests
import json
from newsapi import NewsApiClient

# key=NewsApiClient(api_key='0e7da5e0c4f04b5384567b318fdb121a"')
app = Flask(__name__)


@app.route('/news', methods=['get'])
def BBC():
    url = "https://newsapi.org/v1/sources?language=en"
    # url="https://newsapi.org/v1/sources?language=en&apiKey=0e7da5e0c4f04b5384567b318fdb121a"
    # url = "https://newsapi.org/v1/articles?source=bbc-news&language=en&sortBy=top&apiKey=0e7da5e0c4f04b5384567b318fdb121a"
    # url="https://newsapi.org/v2/everything?domains=wsj.com&apiKey=0e7da5e0c4f04b5384567b318fdb121a"
    # url="https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=0e7da5e0c4f04b5384567b318fdb121a"
    open_bbc_page = requests.get(url).json()
    # print(open_bbc_page)
    # article=open_bbc_page["articles"]

    results = [open_bbc_page]

    # for ar in article:
    #      results.append(ar["title"])
    #
    # for i in range(len(results)):
    #     total=results[i]
    #     print(i+1,total)
    return json.dumps(results)


if __name__ == '__main__':
    # BBC()
    app.run()