# models/text2gloss_transformer.py
"""
Placeholder tokenizer/model file.
This is not a trained model — just a minimal helper to keep code running.
"""

class SimpleTokenizer:
    def __init__(self):
        self.vocab = {}

    def fit_on_texts(self, texts):
        # build simple vocab
        idx = 1
        for t in texts:
            for w in t.split():
                if w not in self.vocab:
                    self.vocab[w] = idx
                    idx += 1

    def texts_to_sequences(self, texts):
        return [[self.vocab.get(w, 0) for w in t.split()] for t in texts]

class Text2GlossModel:
    def __init__(self):
        pass

    def predict(self, texts):
        # placeholder: returns uppercase words as gloss
        return [[w.upper() for w in t.split()] for t in texts]
