import spacy
nlp = spacy.load("en_core_web_sm")

def preprocess(text):
    doc = nlp(text.lower())
    result = []
    for token in doc:
        if not token.is_stop:
            result.append(token.lemma_)
    return "".join(result)