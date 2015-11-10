import urllib, json
from flask import Flask, render_template

app = Flask(__name__)

#search = 'banana'
#searchEncoded = urllib.quote(search)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/t")
@app.route("/t/<tag>")
def t(tag="america"):#searchEncoded):
    #searchEncoded = urllib.quote(tag)
    #rawData = urllib.urlopen('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q='+searchEncoded).read()
    key="6qjbDDaQ4vUogvpFIZ2UoaHuo6ykn1vMpjRYOdYOPCQI6dBw4K"
    uri="https://api.tumblr.com/v2/tagged?tag=%s&api_key=%s"
    url = uri%(tag,key)

    request = urllib2.urlopen(url)
    rawData = request.read()
    jsonData = json.loads(rawData)
    
    searchResults = jsonData['responseData']['results']
    images = []
    for results in searchResults:
        try:
            images.append(['photos'][0]['original_size']['url'])#results['url'])
        except:
            pass
    return render_template("images.html",urls=images);

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=9000)
