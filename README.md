# 🌐 Multi-Language Translator

A beautiful and responsive web application for translating text between multiple Indian languages using Google Translate API. Built with Flask and modern web technologies.

## ✨ Features

- **Multi-language Support**: Translate between 11 languages including Hindi, Kannada, Tamil, Telugu, Bengali, English, Marathi, Gujarati, Malayalam, Punjabi, and Urdu
- **Beautiful UI**: Modern, responsive design with gradient backgrounds and smooth animations
- **Font Support**: Optimized typography for Indic scripts with Noto Sans font family
- **Real-time Translation**: Fast and accurate translations powered by Google Translate
- **Interactive Controls**: Language swap, copy to clipboard, and clear functions
- **Font Testing**: Built-in Kannada font testing feature
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Error Handling**: Comprehensive error handling with user-friendly messages

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone or download the project files**
   ```bash
   # Create project directory
   mkdir multi-language-translator
   cd multi-language-translator
   ```

2. **Set up the project structure**
   ```
   Gen AI/
   ├── app.py                  # Main Flask application
   ├── requirement.txt         # Dependencies
   └── templates/
       └── index.html          # Frontend template
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirement.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open in browser**
   ```
   http://localhost:5000
   ```

## 📦 Dependencies

The application requires the following Python packages:

```
Flask==2.3.3
deep-translator==1.11.4
```

## 🎯 Usage

### Basic Translation

1. **Select Source Language**: Choose the language of your input text
2. **Select Target Language**: Choose the language you want to translate to
3. **Enter Text**: Type or paste your text in the input area
4. **Translate**: Click "Translate Text" or press Ctrl+Enter
5. **Copy Result**: Use the "Copy Result" button to copy the translation

### Advanced Features

- **Language Swap**: Click the ⇄ button to quickly swap source and target languages
- **Font Selection**: Choose from different Noto Sans fonts for better Indic script display
- **Kannada Testing**: Use the "Test Kannada" button to verify font rendering
- **Clear All**: Reset both input and output areas

## 🔧 API Endpoints

### `GET /`
- **Description**: Renders the main translator page
- **Response**: HTML page with the translator interface

### `POST /translate`
- **Description**: Handles translation requests
- **Request Body**:
  ```json
  {
    "text": "Text to translate",
    "source_lang": "English",
    "target_lang": "Hindi"
  }
  ```
- **Response**:
  ```json
  {
    "success": true,
    "translated_text": "Translated text",
    "source_lang": "English",
    "target_lang": "Hindi"
  }
  ```

### `GET /test_kannada`
- **Description**: Returns sample Kannada text for font testing
- **Response**:
  ```json
  {
    "sample_text": "Sample Kannada text",
    "message": "Kannada font test sample"
  }
  ```

## 🌍 Supported Languages

| Language | Code | Script |
|----------|------|---------|
| English | en | Latin |
| Hindi | hi | Devanagari |
| Kannada | kn | Kannada |
| Tamil | ta | Tamil |
| Telugu | te | Telugu |
| Bengali | bn | Bengali |
| Marathi | mr | Devanagari |
| Gujarati | gu | Gujarati |
| Malayalam | ml | Malayalam |
| Punjabi | pa | Gurmukhi |
| Urdu | ur | Arabic |

## 🎨 Design Features

- **Modern UI**: Clean, intuitive interface with gradient backgrounds
- **Responsive Layout**: Adapts to different screen sizes
- **Typography**: Optimized fonts for Indic scripts
- **Animations**: Smooth transitions and hover effects
- **Status Bar**: Real-time feedback on application status
- **Error Handling**: User-friendly error messages

## 🔧 Technical Details

### Frontend Technologies
- **HTML5**: Semantic markup
- **CSS3**: Modern styling with flexbox and grid
- **JavaScript**: ES6+ features for interactivity
- **Google Fonts**: Noto Sans font family for Indic scripts

### Backend Technologies
- **Flask**: Lightweight Python web framework
- **deep-translator**: Google Translate API integration
- **JSON**: Data exchange format

### Key Features
- **CORS Ready**: Can be easily configured for cross-origin requests
- **Error Handling**: Comprehensive error handling on both frontend and backend
- **Validation**: Input validation and sanitization
- **Encoding**: Proper UTF-8 encoding for multilingual support

## 🚀 Deployment

### Local Development
```bash
python app.py
```
The application will run on `http://localhost:5000` with debug mode enabled.

### Production Deployment
For production deployment, consider:
- Using a WSGI server like Gunicorn
- Setting up a reverse proxy with Nginx
- Configuring environment variables
- Implementing proper logging

Example with Gunicorn:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## 📱 Browser Compatibility

- **Chrome**: 70+
- **Firefox**: 65+
- **Safari**: 12+
- **Edge**: 79+

## 🤝 Contributing

1. Fork the project
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request


## 🐛 Known Issues

- Translation accuracy depends on Google Translate API
- Some complex text formatting may not be preserved
- Font rendering may vary across different operating systems

## 🆘 Support

For issues or questions:
1. Check the browser console for error messages
2. Verify internet connection for translation API
3. Ensure all dependencies are properly installed
4. Check Python version compatibility

## 🔮 Future Enhancements

- [ ] Add more languages
- [ ] Implement offline translation
- [ ] Add text-to-speech functionality
- [ ] Include translation history
- [ ] Add file upload support
- [ ] Implement user authentication
- [ ] Add translation confidence scores
- [ ] Support for document translation

---
