#load dependencies
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
from data_load import data

# Embedding model - sentence-transformers (https://www.sbert.net/docs/sentence_transformer/pretrained_models.html)
model = SentenceTransformer('multi-qa-mpnet-base-cos-v1') #added semantic-search specific model
# model = SentenceTransformer('all-MiniLM-L6-v2')
text_column = 'Text' #text column can be updated based on input CSV/data object

# Generate embeddings
def generate_embeddings(df, text_column):
    return model.encode(df[text_column].tolist(), convert_to_tensor=True)

#function to generate vector store - FAISS & create index
def embedding_vectorstore():
    embeddings = generate_embeddings(data, text_column)

    # Convert to numpy for FAISS
    embedding_matrix = np.array([embedding.numpy() for embedding in embeddings])

    # Create FAISS index
    index = faiss.IndexFlatL2(embedding_matrix.shape[1])
    index.add(embedding_matrix)


def display_info():
        embedding_vectorstore()
        return "Data loaded into vector store"

