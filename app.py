import urllib2,json
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

#@app.route("/anime

@app.route("/t")
@app.route("/t/<tag>")
def t(tag="search"):
    url="http://myanimelist.net/api/anime/search.xml?tag=%s"
    request = urllib2.urlopen(url)
    result = request.read()
    r = json.loads(result)
    moviePosters = []
    for poster in r["response"]:
        try:
            moviePosters.append(poster["image_url"])
        except:
            pass

    return render_template("moviePosters.html", urls=moviePosters)


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=9000)
