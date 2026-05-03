import os
from flask import Flask, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import traceback # Tambahkan ini untuk debugging

load_dotenv()

app = Flask(__name__)

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise Exception("GEMINI_API_KEY belum diisi di .env")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("models/gemini-flash-latest")


@app.route("/")
def home():
    return "PinkNotes AI Backend Running"


@app.route("/generate-title", methods=["POST"])
def generate_title():
    try:
        data = request.get_json()
        note_content = data.get("note_content", "").strip()

        if not note_content:
            return jsonify({
                "error": "note_content kosong"
            }), 400

        prompt = f"""
Buatkan judul catatan singkat,
maksimal 6 kata,
berdasarkan isi berikut:

{note_content}

Jawab judul saja.
"""

        response = model.generate_content(prompt)

        title = response.text.strip().replace('"', "")

        return jsonify({
            "generated_title": title
        })

    except Exception as e:
        # --- Bagian ini diperbarui untuk mencetak traceback lengkap ---
        print(f"Error occurred in /generate-title: {e}")
        traceback.print_exc() # Ini akan mencetak traceback lengkap ke konsol
        # --- Akhir bagian yang diperbarui ---
        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    print("=== PinkNotes Backend Running ===")
    print("LAN URL: http://192.168.0.30:5055")

    app.run(
        host="0.0.0.0",
        port=5055,
        debug=False
    )
