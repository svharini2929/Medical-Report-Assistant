import re

def format_medical_text(text):
    """Cleans up LLM output for Streamlit rendering."""
    cleaned_text = text.strip()
    # Replace newlines with HTML line breaks for the result card
    cleaned_text = cleaned_text.replace("\n", "<br>")
    return cleaned_text

def bold_biomarkers(text):
    """Bolds common medical terms for better readability."""
    keywords = [
        'Hemoglobin', 'Glucose', 'Cholesterol', 'RBC', 'WBC', 'Iron',
        'Platelets', 'Creatinine', 'Sodium', 'Potassium', 'Calcium',
        'Bilirubin', 'Albumin', 'Thyroid', 'TSH', 'HbA1c'
    ]
    for word in keywords:
        text = re.sub(f"({word})", r"<b>\1</b>", text, flags=re.IGNORECASE)
    return text

def get_mandatory_disclaimer():
    """Returns the legal disclaimer for medical AI projects."""
    return (
        "This AI-generated explanation is for educational purposes only. "
        "It is NOT a medical diagnosis. Lab results should always be interpreted "
        "by a qualified healthcare professional. Do not make health decisions "
        "based on this output."
    )

def calculate_bmi(weight_kg, height_m):
    if height_m > 0:
        return round(weight_kg / (height_m ** 2), 2)
    return 0