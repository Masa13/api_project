import urllib, json
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

#search = 'banana'
#searchEncoded = urllib.quote(search)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/browse", methods=["GET", "POST"])
@app.route("/browse/", methods=["GET", "POST"])
def browse():
    if request.method == "GET":
        return render_template("search.html")
    else:
        keyword1=request.form['keyword1']
        keyword2=request.form['keyword2']
        search=keyword1+" "+keyword2
        searchEncoded = urllib.quote(search)
        rawData = urllib.urlopen("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="+tag).read()
        jsonDATA = json.loads(rawData)
        searchResults = jsonDATA["responseData"]["results"]
        images = []
        for result in searchResults:
            try:
                images.append(result['url'])
            except:
                pass
        return render_template("images.html", urls=images)
            
        
#@app.route("/search")
#@app.route("/search/<tag>")
#def t(tag=searchEncoded):
#    rawData = urllib.urlopen("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="+tag).read()
#    jsonDATA = json.loads(rawData)
#    searchResults = jsonDATA["responseData"]["results"]
#    images = []
#    for result in searchResults:
#        try:
#            images.append(result['url'])
#        except:
#            pass
#    return render_template("images.html",urls=images)


if (__name__ == "__main__"):
   app.debug = True
   app.run(host="0.0.0.0", port=9000)
