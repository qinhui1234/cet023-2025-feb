from flask import Flask 
from flask import request,render_template
import google.generativeai as genai
import os
import textblob

api = os.getenv("makersuite")

genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-1.5-flash')

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
   return(render_template("index.html"))

@app.route("/makersuite",methods=["GET","POST"])
def makersuite():
   return(render_template("makersuite.html"))

@app.route("/gemini",methods=["GET","POST"])
def gemini():
   q = request.form.get("q")
   r = model.generate_content(q)
   return

@app.route("/sentiment",methods=["GET","POST"])
def sentiment():
   return(render_template("sentiment.html"))

@app.route("/textblob_result",methods=["GET","POST"])
def textblob_result():
   q = request.form.get("q")
   r = textblob.TextBlob(q).sentiment
   return(render_template("textblob_result.html",r=r))

if __name__ == "__main__":
    app.run()