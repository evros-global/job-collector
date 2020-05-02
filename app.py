from flask import Flask, render_template, url_for, redirect, request, send_file
import os
app=Flask(__name__)

@app.route("/")
def base():
  options=[i for i in range(1,51)]
  return render_template('base.html', options=options)

@app.route('/', methods=['POST'])
def returnFile():
  job=request.form["inputJob"]
  location=request.form["location"]
  downloadType=request.form["downloadType"]
  numberOfPages=request.form['numberOfPages']
  #scrapy crawl indeed -o indeed.csv -a job="" -a location="" -a pages=2
  if(downloadType=='JSON'):
    #os.popen('scrapy crawl indeed -o indeed.json -a attr="'+job+'-'+location+'"')
    os.system('del indeed.json')
    os.system('scrapy crawl indeed -o indeed.json -a job="'+job+'" -a location="'+location+'" -a pages='+str(numberOfPages))
    return send_file("indeed.json")
  else:
    #os.popen('scrapy crawl indeed -o indeed.csv -a attr="'+job+'-'+location+'"')
    os.system('del indeed.csv')
    os.system('scrapy crawl indeed -o indeed.csv -a job="'+job+'" -a location="'+location+'" -a pages='+str(numberOfPages))
    return send_file("indeed.csv")
  


if __name__=="__main__":
  app.run(debug=True)
