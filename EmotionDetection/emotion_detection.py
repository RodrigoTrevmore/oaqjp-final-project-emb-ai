"""
This module will handle the text submited for analysis
using Emotion Predict function from Wtson NLP library
"""
import json
import requests

def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json = myobj, headers = headers, timeout = 5000)
    formatted_response = json.loads(response.text)

    if response.status_code == 200:
        new_reponse = formatted_response['emotionPredictions'][0]['emotion']
        dominant_emotion = max(new_reponse, key=new_reponse.get)
        new_reponse["dominant_emotion"] = dominant_emotion
        return new_reponse
    elif response.status_code == 400:
        empty_response = {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
            }
        return empty_response
