from flask import Flask
import argparse

app = Flask(__name__)


@app.route("/")
def hello_world():
    name = app.config.get("NAME", "world")
    return f"<p>Hello, {name}!</p>"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="运行 Flask 应用并设置问候名称")
    parser.add_argument("--name", default="world", help="要问候的姓名（默认: world）")
    args = parser.parse_args()
    app.config["NAME"] = args.name
    app.run(host="0.0.0.0", port=5000)

