from sentence_transformers import SentenceTransformer
import numpy as np
import os

# Load the example document
with open("data/example_doc.txt", "r") as file:
    text = file.read()

# Split the text into simple chunks (can use LangChain or custom logic)
chunk_size = 300
chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

print(f"Total chunks created: {len(chunks)}")

# Load a Sentence Transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")  # small & fast

# Generate embeddings
embeddings = model.encode(chunks)

# Save embeddings as .npy
os.makedirs("embeddings", exist_ok=True)
np.save("embeddings/doc_embeddings.npy", embeddings)

# Save the chunks as well for later retrieval
with open("embeddings/doc_chunks.txt", "w") as f:
    for chunk in chunks:
        f.write(chunk + "\n---\n")

print("✅ Embeddings and chunks saved.")
