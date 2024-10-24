from flask import Flask, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main_():
    if request.method == "GET":
        return "Flask is corriendo."
    
    # Para solicitudes POST, se espera el texto para traducir
    data = request.get_json()
    if 'text' not in data:
        return "No text provided", 400

    text = data['text']
    try:
        translated_text = GoogleTranslator(source='en', target='es').translate(text)
        
        # Devolver el texto traducido como texto plano
        return translated_text
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    app.run(debug=True)