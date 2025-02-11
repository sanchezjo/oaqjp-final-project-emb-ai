
import requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data_json = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = data_json, headers = headers)

    status_code = response.status_code
    print(status_code)

    if status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
             }

    # format and extract emotions
    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]

    # build return type
    scores = {
    "anger": emotions.get("anger", 0),
    "disgust": emotions.get("disgust", 0),
    "fear": emotions.get("fear", 0),
    "joy": emotions.get("joy", 0),
    "sadness": emotions.get("sadness", 0),
    }

    # add dominant emotion
    dominant_emotion = max(scores, key=scores.get)
    scores["dominant_emotion"] = dominant_emotion
    
    return scores

