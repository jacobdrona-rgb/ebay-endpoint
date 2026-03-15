import hashlib
from flask import Flask, request, jsonify

app = Flask(__name__)

VERIFICATION_TOKEN = "RonaCollectibles-ebay-token-2024"
ENDPOINT_URL = "https://ebay-endpoint-dcje.onrender.com/ebay-deletion"

@app.route("/ebay-deletion", methods=["GET", "POST"])
def ebay_deletion():
    if request.method == "GET":
        challenge_code = request.args.get("challenge_code", "")
        h = hashlib.sha256()
        h.update(challenge_code.encode("utf-8"))
        h.update(VERIFICATION_TOKEN.encode("utf-8"))
        h.update(ENDPOINT_URL.encode("utf-8"))
        return jsonify({"challengeResponse": h.hexdigest()})
    return "", 200

if __name__ == "__main__":
    app.run()
