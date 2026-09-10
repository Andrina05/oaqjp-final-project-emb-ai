"""
Python function to make an HTTP request
to Emotion Predict function of the Watson
NLP library, and extract data about the
nature of given text.
"""

import requests
import json

def emotion_detector(text_to_analyze):
    # URL to send request to
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Request headers
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Input JSON
    my_obj = { "raw_document": { "text": text_to_analyze } }

    # Make a POST request and obtain a response object
    response = requests.post(url, json=my_obj, headers=header)

    # Check for successful response
    if response.status_code == 200:
        formatted_text = json.loads(response.text)
        emotions = formatted_text["emotionPredictions"][0]["emotion"]
        
        # Find the emotion with the highest score
        dominant_emotion = None
        max_score = 0
        for emotion, score in emotions.items():
            dominant_emotion = emotion if score > max_score else dominant_emotion
            max_score = max(max_score, score)
        
        # Check if dominant_emotion has been set to a non-null value
        if dominant_emotion != None:
            emotions["dominant_emotion"] = dominant_emotion

            return emotions
