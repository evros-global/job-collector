from flask import Flask, send_file, request
from indeed import *

app = Flask(__name__)

@app.route('/')
def main():
   options ='\n'.join(['<option value="{}">{}</option>'.format(i,i)  for i in range(1,50)])
     
   return """
<form method=POST>
indeed url: <input name="url" size="100"></input> <br>
<b>Example url:</b> https://www.indeed.com/jobs?q=social+media&l=United+States&explvl=entry_level&remotejob=1 </br><br>
number of pages: 
<select name="num_pages"> """ + options + """
</select><br><br>
<input type=submit></input><br>
Please click submit only once and wait for the file to be downloaded
</form>
"""

@app.route('/', methods=["POST"])
def return_file():
  scrape_indeed(request.form['url'], int(request.form['num_pages']))
  return send_file("newcsv.csv")
