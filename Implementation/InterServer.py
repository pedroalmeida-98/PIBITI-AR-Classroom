from flask import Flask, render_template, request, jsonify
import socket
import requests

celpeu = '172.20.10.4'
pclab = '172.20.9.110'
local ='127.0.0.1'
app = Flask(__name__, static_folder = 'static')

# criar a primeira página do site

if __name__ == "__main__":
    app.run()

@app.route("/")
def home():
    return render_template("index.html")

