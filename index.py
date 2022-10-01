from flask import Flask, render_template, request
from googlesearch import search


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def getvalue():
    search = request.form['search']
    search_list=pdfsearch(search)
    return render_template('pdfurl.html',search=search,search_list=search_list)

def pdfsearch(keyword):
    name=keyword
    # to search
    query = name+" filetype:pdf"
    print(query)
    ar = [] 
    for j in search(query, tld="co.in", num=10, stop=10, pause=1):
        ar.append(j)
    return ar
