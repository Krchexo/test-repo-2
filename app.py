from flask import Flask
from concat import concat

app = Flask(__name__)

# Expected: "foobar"
print(concat("foo", "bar"))

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
