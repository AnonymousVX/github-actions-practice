import os
from flask import Flask, jsonify, request

# Flask app

app = Flask(__name__)
# Load secret key from environment for security (never hardcode in production)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(24))


@app.route("/health", methods=["GET"])
def health_check():
    """Health check endpoint for monitoring."""
    return jsonify({"status": "healthy"}), 200


@app.route("/api/greet", methods=["POST"])
def greet_user():
    """Accepts JSON payload and returns a personalized greeting."""
    data = request.get_json(silent=True) or {}
    name = data.get("name", "World")
    return jsonify({"message": f"Hello, {name}!"}), 200



if __name__ == "__main__":
    # Set debug=False in production environments
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)
