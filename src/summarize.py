import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

_model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

def embed(sentences:list[str])->np.ndarray:
    return _model.encode(sentences, normalize_embeddings=True)

def mmr(sentences:list[str], k:int=5, lambda_:float=0.6):
    # centroid-based MMR over sentence embeddings
    E = embed(sentences)
    centroid = E.mean(axis=0, keepdims=True)
    sim_to_centroid = cosine_similarity(E, centroid).ravel()
    selected, candidates = [], list(range(len(sentences)))
    # pick the most central first
    first = int(np.argmax(sim_to_centroid))
    selected.append(first); candidates.remove(first)
    while len(selected)<min(k, len(sentences)) and candidates:
        mmr_scores = []
        for c in candidates:
            relevance = sim_to_centroid[c]
            redundancy = max(cosine_similarity(E[c:c+1], E[selected]).ravel())
            mmr_scores.append(lambda_*relevance - (1-lambda_)*redundancy)
        best_idx = candidates[int(np.argmax(mmr_scores))]
        selected.append(best_idx); candidates.remove(best_idx)
    return [sentences[i] for i in selected]