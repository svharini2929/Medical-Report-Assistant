import os
import pandas as pd # You might need to run: pip install pandas
from src.rag_logic import RAGManager

def digest_csv(file_path):
    """Parses health_markers_dataset.csv and returns a list of text chunks."""
    print(f"📖 Reading: {file_path}")
    df = pd.read_csv(file_path)
    
    medical_facts = []
    
    # We combine all columns into a descriptive sentence for each row
    for index, row in df.iterrows():
        # This assumes your CSV has columns like 'Marker', 'Normal Range', etc.
        # It creates a string for each row to feed into the AI's memory
        fact = " | ".join([f"{col}: {val}" for col, val in row.items()])
        medical_facts.append(fact)
            
    return medical_facts

def run_ingestion():
    rag = RAGManager()
    
    # Update this to match your EXACT file name in the data folder
    csv_file = os.path.join("data", "health_markers_dataset.csv")
            
    if os.path.exists(csv_file):
        facts = digest_csv(csv_file)
        print(f"🚀 Found {len(facts)} markers. Loading into Vector DB...")
        rag.add_documents(facts)
        print("✅ Ingestion Complete! Your knowledge base is ready.")
    else:
        print(f"❌ Error: Could not find {csv_file}")

if __name__ == "__main__":
    run_ingestion()