from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/final', methods=['POST'])
def final_request():
    data = request.get_json()
    masked_request = data['request']  # You can further process or log the request if needed

    # Here you can implement the logic to handle the Tor installation request
    # For example, you might want to return a message or redirect to a download link
    # This is just a placeholder response
    return jsonify({"message": "Tor installation request received", "details": masked_request})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
