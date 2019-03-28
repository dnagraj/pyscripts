import requests,json

app=Flask(__name__)

# @app.route('/api',methods=['get'])
# def api():
#     url="https://newsapi.org/v1/sources?language=en"
#
#     open_api_page=requests.get(url).json()
#     return json.dumps(open_api_page)
# if __name__=='__main__':
#     app.run()

@app.route('/api/v1',methods=['get'])
def apiv1():
    # results=requests.get("https://newsapi.org/v1/sources?language=en").json()
    results=requests.get("https://newsapi.org/v2/top-headlines?country=in&apiKey=d75db73c5f5043f9807c8e3f400c3afe ").json()
    return json.dumps(results)

if __name__=='__main__':
    app.run()
