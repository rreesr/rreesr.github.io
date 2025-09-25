from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/final', methods=['POST'])
def final_request():
    data = request.get_json()
    masked_request = data['request']  # You can log or process the request if needed

    # Official Tor Project installer links
    tor_installers = {
        "Windows": "https://www.torproject.org/dist/torbrowser/12.5.0/torbrowser-install-win64-12.5.0_en-US.exe",
        "Linux": "https://www.torproject.org/dist/torbrowser/12.5.0/tor-browser-linux64-12.5.0_en-US.tar.xz"
    }

    # You can customize the response message as needed
    response_message = {
        "message": "Tor installation request received",
        "details": masked_request,
        "installers": tor_installers
    }

    return jsonify(response_message)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
