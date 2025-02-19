#load dependencies
import numpy as np
from vector_store import model
from vector_store import index
from data_load import data

# Search function
def search(query, k=1000):
    query_embedding = model.encode([query], convert_to_tensor=True)
    query_embedding = np.array(query_embedding.numpy()).astype(np.float32)
    distances, indices = index.search(query_embedding, k)
    return indices, distances



# Mental health
query = "Find research around mental health"
indices, distances = search(query)

# Retrieve matching records
matching_records_ment_hlth = data.iloc[indices[0]]