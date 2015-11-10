import urllib, json
from flask import Flask, render_template

app = Flask(__name__)

search = 'banana'
searchEncoded = urllib.quote(search)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/t")
@app.route("/t/<tag>")
def t(tag=searchEncoded):
    rawData = urllib.urlopen("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="+tag).read()
    jsonDATA = json.loads(rawData)
    searchResults = jsonDATA["responseData"]["results"]
    images = []
    for result in searchResults:
        try:
            images.append(result['url'])
        except:
            pass
    return render_template("images.html",urls=images)

@app.route("/browse")
@app.route("/browse/<tag>")
def browse(tag="America"):
    key="AIzaSyCMMiZuxl1R8QcMb0SZyvlzyCxNTJO0Zl4"
    uri=""

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=9000)
