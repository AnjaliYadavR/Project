from flask import Flask, render_template, request
from query import askQuery
from waitress import serve

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    print("Index executed")
    return render_template("index.html")


@app.route("/LetsAsk")
def LetsAsk():
    print("letsAsk executed")
    query = request.args.get("query")
    query = query.strip()
    print(f"Query is - {query}")
    if not bool(query):
        return render_template("index.html")
    else:
        output = askQuery(query)
        return render_template("LetsAsk.html", result=output)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
