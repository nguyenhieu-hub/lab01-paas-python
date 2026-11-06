from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  return "<h1>Lab 01 PaaS - Deploy on Render</h1><p>Ho va ten: Nguyen Manh Hieu - MSSV: 2324802010220</p>"


if __name__ == "__main__":
  app.run()
