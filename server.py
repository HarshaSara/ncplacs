from flask import Flask

PORT = 8000
MESSAGE = "Hello, world! \n New update for CI  and CD.VERSION CHANGED This is NCPLACR05 app(v-2.0.219). \n"

app = Flask(__name__)


@app.route("/")
def root():
    result = MESSAGE.encode("utf-8")
    return result


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=PORT)
