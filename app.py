from flask import Flask, render_template, request, jsonify
from deep_translator import GoogleTranslator
import json

app = Flask(__name__)

# Define supported languages
LANGUAGES = {
    "Hindi": "hi",
    "Kannada": "kn", 
    "Tamil": "ta",
    "Telugu": "te",
    "Bengali": "bn",
    "English": "en",
    "Marathi": "mr",
    "Gujarati": "gu",
    "Malayalam": "ml",
    "Punjabi": "pa",
    "Urdu": "ur"
}

@app.route('/')
def index():
    """Render the main translator page"""
    return render_template('index.html', languages=LANGUAGES)

@app.route('/translate', methods=['POST'])
def translate():
    """Handle translation requests"""
    try:
        data = request.get_json()
        
        input_text = data.get('text', '').strip()
        source_lang = data.get('source_lang', 'English')
        target_lang = data.get('target_lang', 'Hindi')
        
        # Validation
        if not input_text:
            return jsonify({'error': 'Please enter some text to translate!'}), 400
            
        if source_lang == target_lang:
            return jsonify({'error': 'Source and target languages cannot be the same!'}), 400
            
        if source_lang not in LANGUAGES or target_lang not in LANGUAGES:
            return jsonify({'error': 'Invalid language selection!'}), 400
        
        # Get language codes
        source_code = LANGUAGES[source_lang]
        target_code = LANGUAGES[target_lang]
        
        # Perform translation
        translator = GoogleTranslator(source=source_code, target=target_code)
        translated_text = translator.translate(input_text)
        
        # Ensure proper encoding
        if isinstance(translated_text, str):
            try:
                translated_text = translated_text.encode('utf-8').decode('utf-8')
            except (UnicodeEncodeError, UnicodeDecodeError):
                pass
        
        return jsonify({
            'success': True,
            'translated_text': translated_text,
            'source_lang': source_lang,
            'target_lang': target_lang
        })
        
    except Exception as e:
        return jsonify({'error': f'Translation failed: {str(e)}'}), 500

@app.route('/test_kannada')
def test_kannada():
    """Return sample Kannada text for font testing"""
    sample_text = """ಭಾರತವು ಶ್ರೀಮಂತ ಮತ್ತು ವೈವಿಧ್ಯಮಯ ಇತಿಹಾಸವನ್ನು ಹೊಂದಿದೆ, ಅದು ಸಾವಿರಾರು ವರ್ಷಗಳ ಹಿಂದಿನದು.

ಸಿಂಧೂ ಕಣಿವೆ ನಾಗರಿಕತೆ ಸೇರಿದಂತೆ ವಿಶ್ವದ ಕೆಲವು ಆರಂಭಿಕ ನಾಗರಿಕತೆಗಳಿಗೆ ಇದು ನೆಲೆಯಾಗಿದೆ."""
    
    return jsonify({
        'sample_text': sample_text,
        'message': 'Kannada font test sample'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
