import chromadb
from sentence_transformers import SentenceTransformer
import uuid

class RAGManager:
    def __init__(self, db_path="./vector_db"):
        self.client = chromadb.PersistentClient(path=db_path)
        self.collection = self.client.get_or_create_collection(name="medical_knowledge")
        # We name this self.model so it matches your ingest_data script
        self.model = SentenceTransformer('all-MiniLM-L6-v2') 

    def add_documents(self, text_list):
        """Adds medical facts to the database in batches for speed."""
        batch_size = 100
        total = len(text_list)
        
        for i in range(0, total, batch_size):
            batch = text_list[i : i + batch_size]
            
            # Generate embeddings for the whole batch at once
            embeddings = self.model.encode(batch).tolist()
            ids = [str(uuid.uuid4()) for _ in range(len(batch))]
            
            self.collection.add(
                ids=ids,
                embeddings=embeddings,
                documents=batch
            )
            print(f"⏳ Progress: {i + len(batch)}/{total} markers loaded...")

    def query_knowledge(self, query_text, n_results=3):
        """Retrieves relevant facts from the DB."""
        query_vector = self.model.encode(query_text).tolist()
        results = self.collection.query(query_embeddings=[query_vector], n_results=n_results)
        return " ".join(results['documents'][0]) if results['documents'] else ""