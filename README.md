# X-Gem AI

Simple AI chatbot based on `https://text.pollinations.ai/` with both terminal and
web interfaces.  You can run it locally or deploy the backend as a serverless
function (Vercel support is already prepared).

## Features

- **CLI mode**: `python ai.py` runs a read/eval loop in the terminal.
- **Web UI**: a minimal single‑page chat interface served by Flask.
- **API endpoint**: `/api/chat` accepts JSON with `{message: string}` and
  proxies to the AI service.
- Shared logic between CLI and web to keep behaviour consistent.
- CORS enabled so the UI or any other frontend can call the API.

## Getting started

1. **Create a virtual environment** (optional but recommended):
   ```powershell
   cd c:\Users\zayni\Desktop\x-gemaibeta
   python -m venv env
   .\env\Scripts\Activate.ps1
   ```

2. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run in CLI mode**:
   ```powershell
   python ai.py
   ```
   Type messages and the bot will reply; type `exit` to quit.

4. **Start the web server**:
   ```powershell
   python ai.py --web
   ```
   or, if you prefer using Flask's CLI:
   ```powershell
   set FLASK_APP=api/index.py
   flask run
   ```

5. **Open the UI** in your browser at http://127.0.0.1:5000/.  The front end is
   defined in `index.html` and will send requests to `/api/chat`.

6. **API**
   ```http
   POST /api/chat
   Content-Type: application/json
   {
       "message": "Salom"
   }
   ```
   Response JSON looks like:
   ```json
   {
       "success": true,
       "response": "...text from AI..."
   }
   ```

## Deployment

- Deploy the `api` folder as a serverless function (e.g. Vercel) – the last
  line of `api/index.py` (`app = app`) keeps the WSGI app alive.
- The frontend can be hosted on any static site host; it must point to the API
  URL (adjust `fetch('/api/chat', ...)` accordingly).

---

This repository now contains everything you need to take the terminal bot and
turn it into a web product!  Modify styling, swap out the backend AI service,
or add authentication as required.  Good luck building your final product.