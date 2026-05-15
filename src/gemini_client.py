import os
from dotenv import load_dotenv
from groq import Groq

# Standard way to load variables from .env
load_dotenv() 

class GeminiAssistant:
    def __init__(self):
        # Pulls the key we renamed in your .env file
        api_key = os.getenv("GROQ_API_KEY")
        
        if not api_key:
            raise ValueError("GROQ_API_KEY not found. Please check your .env file.")
        
        self.client = Groq(api_key=api_key)
        self.model_name = "llama-3.3-70b-versatile"

    def get_explanation(self, extracted_text, retrieved_facts):
        """
        This is the function app.py was missing! 
        It sends the OCR text and RAG context to Groq.
        """
        try:
            prompt = f"""
            ROLE: You are a professional Medical Assistant.
            IMPORTANT: Start your response with "NOT MEDICAL ADVICE. CONSULT A DOCTOR."

            USER REPORT DATA (from OCR): 
            {extracted_text}

            RETRIEVED MEDICAL KNOWLEDGE (from Vector DB): 
            {retrieved_facts}

            TASK: Explain the user's lab results in simple, empathetic language.
            Use the retrieved context to define terms and ranges found in the report.
            """
            
            response = self.client.chat.completions.create(
                model=self.model_name,
                messages=[
                    {"role": "system", "content": "You are a helpful medical assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3, # Keeps the medical facts consistent
                max_tokens=1024
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error generating explanation: {str(e)}"