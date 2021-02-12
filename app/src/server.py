from flask import (
    Flask,
    render_template
)

server = Flask(__name__)

@server.route("/")
def home():
    return  render_template('index.html')

@server.route("/sample")
def sample():
    return "This is sample!"
    
if __name__=="__main__":
  server.run(host='0.0.0.0')