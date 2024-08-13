from flask import Flask, render_template
import os

app=Flask(__name__)

picfolder=os.path.join('static')

app.config['UPLOAD_FOLDER']=picfolder

@app.route('/picture')

def first():
    pic=os.path.join(app.config['UPLOAD_FOLDER'], 'waterfall.jpg')
    return  render_template("home.html", user_image=pic)

@app.route('/second')

def second():
    return  "Welcome to second page"


if __name__=="__main__":
    app.run(debug=True)
