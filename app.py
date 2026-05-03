from flask import Flask, request
from handlers.message_handler import handle_message

app = Flask(__name__)

@app.route("/webhook", methods=["GET", "POST"])
def webhook():
    if request.method == "GET":
        return request.args.get("hub.challenge")

    data = request.json
    handle_message(data)

    return "ok"

if __name__ == "__main__":
    app.run(port=3000)