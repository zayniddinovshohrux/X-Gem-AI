import argparse
import requests
from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os

# shared logic ---------------------------------------------------------------
def get_response(message: str) -> str:
    """Send the user message to the remote AI service and return the text.
    The original terminal version hit pollinations.ai, so we keep the same
    payload for backward compatibility.  More APIs could be added later.
    """
    r = requests.post(
        "https://text.pollinations.ai/",
        json={
            "messages": [{"role": "user", "content": message}],
            "model": "openai",
        },
        timeout=30,
    )
    return r.text

# command‑line interface ----------------------------------------------------
def run_cli():
    print("💭 X-Gem AI (CLI)")
    print("=" * 20)

    while True:
        text = input("\n🧩 User: ")
        if text.strip().lower() == "exit":
            print("🤖 X-Gem: Bye _______________________________👋")
            break

        try:
            answer = get_response(text)
            print(f"\n🤖 X-Gem: {answer}")
        except Exception as e:
            print("⚠️  X-Gem error:", e)

# web application -----------------------------------------------------------
app = Flask(__name__, static_folder='.', static_url_path='')
CORS(app)

@app.route('/api/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'GET':
        return jsonify({'status': 'online', 'message': 'X-Gem AI API ishlayapti'})

    data = request.get_json() or {}
    user_message = data.get('message', '')

    try:
        response_text = get_response(user_message)
        return jsonify({'success': True, 'response': response_text})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/')
def serve_index():
    # serve the local index.html file so the front‑end can be opened via
    # `http://localhost:5000/` rather than using the filesystem.
    return send_from_directory(app.static_folder, 'index.html')

# when the file is executed directly we choose between CLI and web server ------
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='X-Gem AI runner')
    parser.add_argument('--web', action='store_true', help='start HTTP server')
    parser.add_argument('--host', default='127.0.0.1', help='listening host')
    parser.add_argument('--port', type=int, default=5000, help='listening port')
    parser.add_argument('--debug', action='store_true', help='enable Flask debug')
    args = parser.parse_args()

    if args.web:
        # start the same app defined in api/index.py (compatibility kept)
        app.run(host=args.host, port=args.port, debug=args.debug)
    else:
        run_cli()
