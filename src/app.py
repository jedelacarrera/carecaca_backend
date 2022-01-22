import os
from flask import Flask, jsonify, request
from flask_cors import CORS
from pusher import Pusher

from src.enums import CardOrigin
from src.models.table import Table
from src.models.card import Card

app = Flask(__name__)
CORS(app, support_credentials=False, resources={r"/*": {"origins": "*"}})
pusher_client = Pusher(
    ssl=True,
    app_id="1326635",
    key="9ba9d78bd91108bb3657",
    secret=os.getenv("PUSHER_SECRET"),
    cluster="sa1",
)

PUSHER_CHANNEL = "carecaca"


def trigger_event(table_name: str, message: str = "") -> None:
    pusher_client.trigger(PUSHER_CHANNEL, table_name, message)


@app.route("/game/<table_name>/login/<username>", methods=["GET", "POST"])
def login_to_table(table_name: str, username: str):
    table = Table.load_from_folder(table_name)
    table.add_player(username)
    trigger_event(table_name, f"{username} se unió al juego")
    return jsonify(game=table.to_output_request(), status=True)


@app.route("/game/<table_name>", methods=["GET"])
def get_table(table_name: str):
    table = Table.load_from_folder(table_name)
    return jsonify(game=table.to_output_request(), status=True)


@app.route("/game/<table_name>/start", methods=["GET", "POST"])
def start_table(table_name: str):
    try:
        table = Table.load_from_folder(table_name)
        table.deal()
        trigger_event(table_name, "Se repartieron las cartas")
        return jsonify(game=table.to_output_request(), status=True)
    except Exception as e:
        print(str(e))
        return jsonify(status=False, message=str(e))


@app.route("/game/<table_name>/play/<username>", methods=["GET", "POST"])
def play_cards(table_name: str, username: str):
    cards = [Card(**card_data) for card_data in request.json["cards"]]
    cards_str = ", ".join([card.to_json()["rank"] for card in cards])
    try:
        table = Table.load_from_folder(table_name)
        origin = CardOrigin[request.json["origin"]]

        table.play_cards(cards, username, origin)
        message = f"{username} jugó carta(s) ({cards_str}) correctamente"
        if len(table.played_cards) == 0:
            message += ". Se quemó el montón"
        trigger_event(table_name, message)
        return jsonify(game=table.to_output_request(), status=True, ok=True)
    except Exception as e:
        print(str(e))
        message = f"{username} jugó carta(s) ({cards_str}) incorrectamente. ¿Debería llevarse el montón?"
        trigger_event(table_name, message)
        return jsonify(status=False, message=str(e))


@app.route(
    "/game/<table_name>/play_cards_or_take_played_cards/<username>",
    methods=["GET", "POST"],
)
def play_cards_or_take_played_cards(table_name: str, username: str):
    try:
        table = Table.load_from_folder(table_name)
        origin = CardOrigin[request.json["origin"]]
        cards = [Card(**card_data) for card_data in request.json["cards"]]
        cards_str = ", ".join([card.to_json()["rank"] for card in cards])
        message = table.play_cards_or_take_played_cards(cards, username, origin)
        message = f"{username} jugó carta(s) ({cards_str}) " + message
        trigger_event(table_name, message)
        return jsonify(game=table.to_output_request(), status=True, ok=True)
    except Exception as e:
        print(str(e))
        return jsonify(status=False, message=str(e))


@app.route("/game/<table_name>/take_played_cards/<username>", methods=["GET", "POST"])
def take_played_cards(table_name: str, username: str):
    try:
        table = Table.load_from_folder(table_name)
        table.take_played_cards(username)
        message = f"{username} se llevó el montón"
        trigger_event(table_name, message)
        return jsonify(game=table.to_output_request(), status=True, ok=True)
    except Exception as e:
        print(str(e))
        return jsonify(status=False, message=str(e))


@app.route("/", methods=["GET"])
def index():
    return """
        <html>
        <head>
            <link rel="shortcut icon" href="https://flask.palletsprojects.com/en/1.1.x/_static/flask-icon.png">
        </head>
        <body>
            <p>Hola!</p>
            <div id="data"></div>
            <button onclick="makeRequest()">Make Request</button>
            <script>
                const jsonData = {
                    origin: "hand",
                    cards: [{rank: "K", suit: "club"}, {rank: "K", suit: "spade"}]
                }
                function makeRequest() {
                    fetch("/game/game1/take_played_cards/alvaro", {
                        method: "POST",
                        body: JSON.stringify(jsonData),
                        headers: {
                        "Content-Type": "application/json"
                        }
                    }).then(response => {
                        document.getElementById("data").innerHTML = JSON.stringify(response.json());
                    })
                }
                
            </script> 
        </body>
        </html>
    """
