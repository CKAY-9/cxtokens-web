from flask import Flask, render_template, url_for, request, Response
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
    # Overwrite existing data

    if request.method != "POST":
        return Response(status=405)
    
    auth_header = request.headers.get("Authorization")
    if auth_header == None:
        return Response(status=401)
    
    if auth_header != AUTHORIZATION_TOKEN:
        return Response(status=401)
    
    new_player_data = request.form["player_data"]

    data_file = open("./static/data.json", mode="w+")
    data_file.write(new_player_data)
    data_file.close()

    return Response(status=200)
    
@app.get("/api/data")
def get_player_data():
    # Return JSON data

    data_file = open("./static/data.json", mode="r")
    data = json.load(data_file)
    data_file.close()

    return data