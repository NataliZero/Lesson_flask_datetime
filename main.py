from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def show_datetime():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return f"<h1>Текущая дата и время: {now}</h1>"

if __name__ == "__main__":
    app.run()
