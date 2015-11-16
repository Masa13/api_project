import urllib, json, random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

#Default search values
search = 'banana'
searchEncoded = urllib.quote(search)

@app.route("/")
@app.route("/home")
@app.route("/home/")
def home():
    return render_template("home.html")

@app.route("/quiz", methods=["GET","POST"])
@app.route("/quiz/", methods=["GET","POST"])
def quiz():
    #List of words that the user will have to guess
    word_list=['fire','water','earth','galaxy','planet','wise','small','sad','wow','god','stuff','mom','dad','sister','brother','soft','scream','nightmare','america','china','france','england','pokemon','ash','power','death','life','spikes','hairy','pain','exploration']
    search = random.choice(word_list)
    answer=search
    searchEncoded = urllib.quote(search)
    tag=searchEncoded
    rawData = urllib.urlopen("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="+tag).read()
    jsonDATA = json.loads(rawData)
    searchResults = jsonDATA["responseData"]["results"]
    images = []
    for result in searchResults:
        try:
            images.append(result['url'])
        except:
            pass
    if request.method == "GET":
        return render_template("quiz.html",urls=images,result=search)
    else:
        guess=request.form['guess']
        if guess==search:
            return render_template("correct.html")
        else:
            return render_template("incorrect.html",answer=answer)

@app.route("/browse", methods=["GET", "POST"])
@app.route("/browse/", methods=["GET", "POST"])
@app.route("/browse/<tag>", methods=["GET", "POST"])
def browse(tag=searchEncoded):
    if request.method == "GET":
        return render_template("search.html")
    else:
        keyword1=request.form['keyword1']
        keyword2=request.form['keyword2']
        search=keyword1+" "+keyword2
        searchEncoded = urllib.quote(search)
        tag=searchEncoded
        rawData = urllib.urlopen("https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q="+tag).read()
        jsonDATA = json.loads(rawData)
        searchResults = jsonDATA["responseData"]["results"]
        images = []
        for result in searchResults:
            try:
                images.append(result['url'])
            except:
                pass
        return render_template("images.html", urls=images, keyword1=keyword1, keyword2=keyword2)
            



if (__name__ == "__main__"):
   app.debug = True
   app.run(host="0.0.0.0", port=9000)
