# 🩺 Medical Report Assistant

> AI-powered healthcare interpretation system built using RAG (Retrieval-Augmented Generation), OCR, ChromaDB, and Groq-powered LLM inference.

---

## 📌 Overview

Medical reports often contain complex medical terminology that can be difficult for non-medical users to understand.  
This project solves that problem by transforming technical medical reports into simplified, patient-friendly explanations using modern AI technologies.

The system combines:
- Local OCR for text extraction
- Vector database retrieval using ChromaDB
- Retrieval-Augmented Generation (RAG)
- Llama 3.3 70B via Groq API
- Flask full-stack web architecture

Instead of directly generating responses, the assistant first retrieves relevant medical context from a local knowledge base, significantly reducing hallucinations and improving reliability.

---

# 🚀 Features

✅ Upload medical report images  
✅ Local OCR-based text extraction  
✅ Medical knowledge retrieval using ChromaDB  
✅ Context-grounded AI explanations  
✅ Ultra-fast inference using Groq LPUs  
✅ Full-stack Flask web application  
✅ Modular and scalable architecture  
✅ Reduced AI hallucinations with RAG pipeline  
✅ Cost-effective implementation using local processing  

---

# 🧠 How It Works

## Step 1 — OCR Processing
The uploaded medical report image is processed locally using an OCR engine to extract readable medical text.

## Step 2 — Context Retrieval
The extracted text is converted into embeddings and searched against a ChromaDB vector database containing medical information.

## Step 3 — AI Reasoning
The retrieved medical context and report text are combined and sent to Llama 3.3 70B via Groq API.

## Step 4 — Simplified Explanation
The AI generates a simplified, empathetic explanation that users can easily understand.

---

# 🏗️ System Architecture

```text
Medical Report Image
        │
        ▼
   OCR Engine
        │
        ▼
 Extracted Text
        │
        ▼
  ChromaDB Search
        │
        ▼
 Retrieved Context
        │
        ▼
  Llama 3.3 70B
    (Groq API)
        │
        ▼
 Simplified Response
```

---

# 🛠️ Tech Stack

## Backend
- Python
- Flask

## AI / ML
- Retrieval-Augmented Generation (RAG)
- ChromaDB
- Llama 3.3 70B
- Groq API

## OCR
- Local OCR Engine

## Frontend
- HTML
- CSS
- JavaScript

---

# 💡 Why This Project Is Unique

Unlike traditional AI chatbots that directly generate answers, this project uses a Retrieval-Augmented Generation pipeline to retrieve verified medical context before generating explanations.

This improves:
- Accuracy
- Reliability
- Explainability
- User trust

Additionally:
- OCR processing is handled locally
- Groq LPUs provide extremely fast inference
- The architecture is modular and scalable

---

# 📈 Future Improvements

- PDF report support
- Multi-language explanations
- Medical risk highlighting
- User authentication system
- Patient history tracking
- Voice assistant integration
- Cloud deployment
- Fine-tuned medical models

---

# 🎯 Applications

- Healthcare AI Assistants
- Patient Report Interpretation
- Medical AI Research
- AI-Powered Health Platforms
- Clinical Decision Support Systems

---

# 📜 License

This project is intended for educational and research purposes only.

---

# 👩‍💻 Author

## Harini

AI/ML Enthusiast • Developer • Writer

- GitHub: https://github.com/svharini2929
- LinkedIn:https://www.linkedin.com/in/harinisv29/

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.
