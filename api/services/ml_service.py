import pickle
from django.conf import settings

model = None
vectorizer = None


def load_models():
    global model, vectorizer

    if model is None:
        model_path = settings.BASE_DIR / "ml_models" / "risk_model.pkl"

        with open(model_path, "rb") as model_file:
            model = pickle.load(model_file)

    if vectorizer is None:
        vectorizer_path = settings.BASE_DIR / "ml_models" / "risk_vectorizer.pkl"

        with open(vectorizer_path, "rb") as vectorizer_file:
            vectorizer = pickle.load(vectorizer_file)


def predict_text_risk(text):
    load_models()

    text_data = vectorizer.transform([text])
    prediction = model.predict(text_data)[0]
    probability = model.predict_proba(text_data)[0]

    score = round(max(probability) * 100)

    return str(prediction), int(score)
