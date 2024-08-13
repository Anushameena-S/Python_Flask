from flask import Flask

web=Flask(__name__)

@web.route('/')
@web.route('/home')

def home():
    return  "Welcome"

if __name__=="__main__":
    web.run(debug=True)
