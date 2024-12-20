from flask import Flask, render_template, url_for, request
from dotenv import load_dotenv
import os
import json

load_dotenv()

AUTHORIZATION_TOKEN = os.getenv("AUTHORIZATION_TOKEN")

app = Flask(__name__)

@app.get("/")
def index_page():
    return render_template("index.html")

@app.post("/api/update")
def update_player_data():
    if request.method != "POST":
        return
    
    auth_header = request.headers.get("Authorization")
    if auth_header == None:
        return
    
    if auth_header != AUTHORIZATION_TOKEN:
        return
    
    new_player_data = request.form["player_data"]

    data_file = open("./static/data.json", mode="w+")
    data_file.write(new_player_data)
    data_file.close()

    return {"message": "hello"}
    
@app.get("/api/data")
def get_player_data():
    # Return JSON data

    data_file = open("./static/data.json", mode="r")
    data = json.load(data_file)

    return data