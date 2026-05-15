from flask import Flask, request, jsonify, render_template
import os
from dotenv import load_dotenv
from src.rag_logic import RAGManager
from src.gemini_client import GeminiAssistant
from src.ocr_engine import OCREngine
from src.utils import format_medical_text, bold_biomarkers, get_mandatory_disclaimer
from PIL import Image
import io

# 1. Load environment variables from .env
load_dotenv()

# 2. Initialize Flask App
app = Flask(__name__)

# 3. Initialize Engines
# Note: GeminiAssistant now uses Groq internally as per our update
rag_engine = RAGManager()
ai_assistant = GeminiAssistant()
ocr_tool = OCREngine()

@app.route("/")
def index():
    """Serves the main HTML interface."""
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze():
    """Handles the image upload, OCR, RAG retrieval, and AI explanation."""
    if "report" not in request.files:
        return jsonify({"error": "No file uploaded"}), 400

    file = request.files["report"]
    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    try:
        # A. Process Image
        image = Image.open(io.BytesIO(file.read()))

        # B. Local OCR Extraction (Saves Gemini Quota)
        extracted_text = ocr_tool.extract_text(image) 
        
        if not extracted_text or len(extracted_text.strip()) < 5:
            return jsonify({
                "error": "Could not extract clear text. Please ensure the photo is well-lit and clear."
            }), 400

        # C. RAG Knowledge Retrieval
        # Searches your ChromaDB for medical context based on extracted text
        context = rag_engine.query_knowledge(extracted_text)

        # D. Generate Explanation via Groq
        explanation = ai_assistant.get_explanation(extracted_text, context)

        # E. UI Formatting
        formatted = format_medical_text(explanation)
        formatted = bold_biomarkers(formatted)

        return jsonify({
            "success": True,
            "explanation": formatted,
            "disclaimer": get_mandatory_disclaimer()
        })

    except Exception as e:
        # Prints the error to your terminal for debugging
        print(f"Server Error: {str(e)}")
        return jsonify({"error": "An internal error occurred during analysis."}), 500

if __name__ == "__main__":
    # Run the Flask server
    app.run(debug=True, port=5000)