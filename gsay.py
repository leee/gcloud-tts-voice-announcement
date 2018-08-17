import requests
import json
import sys
import base64

key = ''
api = 'https://texttospeech.googleapis.com/v1beta1/text:synthesize'

request_audioconfig = {}
request_audioconfig['audioEncoding'] = 'LINEAR16'
request_audioconfig['pitch'] = '0.00'
request_audioconfig['speakingRate'] = '1.00'

request_voice = {}
request_voice['languageCode'] = 'en-US'
request_voice['name'] = 'en-US-Wavenet-C'

request_input = {}
request_input['text'] = sys.argv[1]

# Create JSON request payload
request = {}
request['audioConfig'] = request_audioconfig
request['voice'] = request_voice
request['input'] = request_input
request_json = json.dumps(request)

url = api + "?key=" + key
headers = {'Content-Type': 'application/json'}
audio_encoded_payload = requests.post(url, headers=headers, data=request_json)
audio_encoded = audio_encoded_payload.json()['audioContent']
audio = base64.b64decode(audio_encoded)
sys.stdout.buffer.write(audio)
