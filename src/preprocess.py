import re, hashlib
import spacy
nlp = spacy.load("en_core_web_sm")
def normalize(text:str)->str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{2,}", "\n\n", text)
    return text.strip()

def to_sentences(text:str):
    doc = nlp(text)
    for i, sent in enumerate(doc.sents):
        s = sent.text.strip()
        if len(s) >= 20:   # drop super-short bits
            yield i, s

def doc_id_from_path(path:str)->str:
    return hashlib.md5(path.encode()).hexdigest()[:8]